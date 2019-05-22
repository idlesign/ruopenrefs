from collections import namedtuple

from .._base import HttpDataProvider, ReferenceBase


class MosOpenDataProvider(HttpDataProvider):
    """Портал открытых данных правительства Москвы.
    https://data.mos.ru

    Для использования API требуется зарегистрироваться и получить ключ,
    который будет передваться в запросах к API.

    * API: https://apidata.mos.ru/
    * Swagger: https://apidata.mos.ru/help/index#/
    * Справочники: https://data.mos.ru/classifier

    """
    alias = 'mosru'
    url_base = 'https://apidata.mos.ru/v1/'

    def __init__(self):
        super().__init__()
        self.key = self._get_setting('KEY')
        self.batch_size = 500
        self.items_limit = None

    def _request_enrich_kwargs(self, **kwargs):

        params = kwargs.get('params', {})
        params.update({
            'api_key': self.key,
        })
        kwargs['params'] = params

        return super()._request_enrich_kwargs(**kwargs)

    def _iter_dataset(self, ref_id: int, *, limit=None, top=None, skip=None):

        params = {}

        limit = limit or self.items_limit
        skip = skip or 0
        top = top or self.batch_size

        if top and limit < top:
            top = limit

        def get_data(top, skip):

            if top:
                params['$top'] = top

            if skip is not None:
                params['$skip'] = skip

            return self.get_data('datasets/%s/rows' % ref_id, params=params)

        count_seen = 0

        if limit is None:
            count_limit = self.get_data('datasets/%s/count' % ref_id)

        else:
            count_limit = limit

        do = True

        while do:

            for item in get_data(top, skip):
                count_seen += 1

                yield item

                if count_seen >= count_limit:
                    do = False

            count_left = count_limit - count_seen

            if count_left < top:
                top = count_left

            skip = count_seen

    def get_data(self, at, **kwargs):
        at = '%s%s' % (self.url_base, at)
        data = super().get_data(at, **kwargs)
        data = data._response.json()
        return data


class MosOpenDataRefBase(ReferenceBase):
    """База справочников."""

    _item_cls = None  # type: namedtuple
    """Тип представляющий записи в справочнике."""

    def __init__(self, *, provider: MosOpenDataProvider = None):
        super().__init__()
        self._provider = provider or MosOpenDataProvider()

    def _cast_item_data(self, data: dict) -> dict:
        raise NotImplementedError

    def dump(self) -> list:
        """Собирает и возвращает все данные справочника."""
        return list(self.iter_items())

    def iter_items(self):
        """Генератор. Позволяет проходить по элементам справочника один за одним."""

        item_cls = self._item_cls
        cast = self._cast_item_data

        for item in self._provider._iter_dataset(self._remote_id):
            yield (item_cls(**cast(item['Cells'])))
