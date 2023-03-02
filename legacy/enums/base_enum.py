from enum import Enum, unique


@unique
class BaseEnum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name
