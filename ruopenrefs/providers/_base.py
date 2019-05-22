from ._http import HttpConnector
from ..settings import get_setting


class DataProvider:
    """База для поставщиков данных."""

    alias = None  # type: str
    """Псевдоним поставщика."""

    _connector_cls = None
    """Класс, реализующий подключение поставщика, взаимодействие с ним."""

    def __init__(self):
        self._connector = self._connector_init()

    def _get_setting(self, name: str) -> str:
        return get_setting('%s_%s' % (self.alias.upper(), name))

    def _connector_init(self):
        connector_cls = self._connector_cls

        connector = None

        if connector_cls:
            connector = connector_cls()

        return connector

    def get_data(self, at):
        raise NotImplementedError


class HttpDataProvider(DataProvider):
    """База для поставщиков данных, получаемых по http(s)."""

    _connector_cls = HttpConnector

    def _request_enrich_kwargs(self, **kwargs):
        return kwargs

    def _request_do(self, to, **kwargs):
        connector = self._connector  # type: HttpConnector
        response = connector.request(to, **self._request_enrich_kwargs(**kwargs))
        return response

    def get_data(self, at, **kwargs):
        return self._request_do(at, **kwargs)


class ReferenceBase:
    """База для описаний справочников."""

    alias = None  # type: str
    _remote_id = None  # type str|int
