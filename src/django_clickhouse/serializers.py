from typing import NamedTuple

import pytz
from django.db.models import Model as DjangoModel

from .utils import model_to_dict


class Django2ClickHouseModelSerializer:
    def __init__(self, model_cls, fields=None, exclude_fields=None, writable=False, defaults=None):
        self._model_cls = model_cls
        if fields is not None:
            self.serialize_fields = fields
        else:
            self.serialize_fields = model_cls.fields(writable=writable).keys()

        self.exclude_serialize_fields = exclude_fields
        self._result_class = self._model_cls.get_tuple_class(defaults=defaults)
        self._fields = self._model_cls.fields(writable=False)

    def _get_serialize_kwargs(self, obj):
        data = model_to_dict(obj, fields=self.serialize_fields, exclude_fields=self.exclude_serialize_fields)

        # Remove None values, they should be initialized as defaults
        result = {
            key: self._fields[key].to_python(value, pytz.utc)
            for key, value in data.items() if value is not None
        }

        return result

    def serialize(self, obj):  # type: (DjangoModel) -> NamedTuple
        return self._result_class(**self._get_serialize_kwargs(obj))
