import pytest

from ruopenrefs.providers.mosru import MosOpenDataProvider, OktmoRef, OkatoRef, OkeiRef, OkvRef, OksmRef

ITEMS_LIMIT = 15

provider = MosOpenDataProvider()
provider.items_limit = ITEMS_LIMIT


def test_export():

    ref = OksmRef(provider=provider)
    data = ref.export()
    assert '),' in data


def test_oksm():

    ref = OksmRef(provider=provider)
    data = list(ref.iter_items())

    assert isinstance(data[0], OksmRef._item_cls)

    dumped = ref.dump()
    assert len(dumped) == ITEMS_LIMIT


def test_okv():

    data = list(OkvRef(provider=provider).iter_items())

    assert isinstance(data[0], OkvRef._item_cls)


def test_oktmo():

    data = list(OktmoRef(provider=provider).iter_items())

    assert isinstance(data[0], OktmoRef._item_cls)


def test_okato():

    data = list(OkatoRef(provider=provider).iter_items())

    assert isinstance(data[0], OkatoRef._item_cls)


def test_okei():

    data = list(OkeiRef(provider=provider).iter_items())

    assert isinstance(data[0], OkeiRef._item_cls)
