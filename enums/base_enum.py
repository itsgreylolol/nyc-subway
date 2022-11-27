from enum import Enum, unique


@unique
class BaseEnum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __repr__(self) -> str:
        """Override basic logging"""
        return f"{self.__class__.__name__}: {self.value}"

    def __str__(self) -> str:
        """Override basic logging"""
        return f"{self.__class__.__name__}: {self.value}"

    @classmethod
    def value_of(cls, value):
        for k, v in cls.__members__.items():
            if k == value:
                return v
        else:
            raise ValueError(f"'{cls.__name__}' enum not found for '{value}'")
