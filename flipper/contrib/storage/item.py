from datetime import datetime
import json
from typing import Optional

from .meta import FeatureFlagStoreMeta


class FeatureFlagStoreItem:
    def __init__(
        self,
        feature_name: str,
        is_enabled: bool,
        meta: FeatureFlagStoreMeta,
    ):
        self.feature_name = feature_name
        self._is_enabled = is_enabled
        self._meta = meta

    def toJSON(self):
        return {
            'feature_name': self.feature_name,
            'is_enabled': self._is_enabled,
            'meta': self._meta.toJSON(),
        }

    def serialize(self) -> bytes:
        return json.dumps(self.toJSON()).encode('utf-8')

    @classmethod
    def deserialize(cls, serialized: bytes):
        deserialized = json.loads(serialized.decode('utf-8'))

        return cls(
            deserialized['feature_name'],
            deserialized['is_enabled'],
            FeatureFlagStoreMeta.fromJSON(deserialized['meta']),
        )

    def is_enabled(self) -> bool:
        return self._is_enabled

    @property
    def meta(self):
        return self._meta.toJSON()