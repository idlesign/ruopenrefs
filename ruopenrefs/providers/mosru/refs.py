from collections import namedtuple

from ._base import MosOpenDataRefBase


class OksmRef(MosOpenDataRefBase):
    """Общероссийский классификатор стран мира (ОКСМ)."""

    alias = 'oksm'
    _remote_id = 2724

    _item_cls = namedtuple(
        'OksmRefItem',
        ('num', 'alfa2', 'alfa3', 'title', 'title_short'))

    def _cast_item_data(self, data: dict) -> dict:
        return dict(
            num=data['CODE'],
            alfa2=data['ALFA2'],
            alfa3=data['ALFA3'],
            title=data['FULLNAME'],
            title_short=data['SHORTNAME'],
        )


class OkvRef(MosOpenDataRefBase):
    """Общероссийский классификатор валют (ОКВ)."""

    alias = 'okv'
    _remote_id = 2293

    _item_cls = namedtuple(
        'OkvRefItem',
        ('num', 'alfa3', 'title', 'country'))

    def _cast_item_data(self, data: dict) -> dict:
        return dict(
            num=data['CODE'],
            alfa3=data['STRCODE'],
            title=data['NAME'],
            country=data['COUNTRY'],
        )


class OktmoRef(MosOpenDataRefBase):
    """Общероссийский классификатор территорий муниципальных образований (ОКТМО)."""

    alias = 'oktmo'
    _remote_id = 2754

    _item_cls = namedtuple(
        'OktmoRefItem',
        ('code', 'title', 'region', 'code_area', 'code_settlement', 'code_local', 'checksum', 'section', 'center', 'hint'))

    def _cast_item_data(self, data: dict) -> dict:
        return dict(
            code=data['CODE'],
            title=data['NAME'],
            region=data['TERRITORY'],
            code_area=data['CODE1'],
            code_settlement=data['CODE2'],
            code_local=data['CODE3'],
            checksum=data['CHECKNUMBER'],
            section=data['SECTION'],
            center=data['CENTRUM'],
            hint=data['DESCRIPTION'],
        )


class OkatoRef(MosOpenDataRefBase):
    """Общероссийский классификатор объектов административно-территориального деления (ОКАТО)."""

    alias = 'okato'
    _remote_id = 2813

    _item_cls = namedtuple(
        'OkatoRefItem',
        ('code', 'title', 'region', 'code_area', 'code_settlement', 'code_local', 'section', 'center'))

    def _cast_item_data(self, data: dict) -> dict:
        return dict(
            code=data['CODE'],
            title=data['NAME'],
            region=data['TERRITORY'],
            code_area=data['CODE1'],
            code_settlement=data['CODE2'],
            code_local=data['CODE3'],
            section=data['SECTION'],
            center=data['CENTRUM'],
        )


class OkeiRef(MosOpenDataRefBase):
    """Общероссийский классификатор единиц измерения (ОКЕИ)."""

    alias = 'okei'
    _remote_id = 2744

    _item_cls = namedtuple(
        'OkeiRefItem',
        ('code', 'title', 'idx', 'section', 'subsection', 'conv_nat', 'conv_iter', 'code_nat', 'code_inter'))

    def _cast_item_data(self, data: dict) -> dict:
        return dict(
            code=data['CODE'],
            title=data['NAME'],
            idx=data['IDX'],
            section=data['SECTION'],
            subsection=data['SUBSECTION'],
            conv_nat=data['NATIONAL'],
            conv_iter=data['INTERNATIONAL'],
            code_nat=data['ALFANATIONAL'],
            code_inter=data['ALFAINTERNATIONAL'],
        )
