from abc import ABC
from enum import Enum, unique


@unique
class BaseEnum(ABC, Enum):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def _generate_next_value_(name, start, count, last_values):
        return name
