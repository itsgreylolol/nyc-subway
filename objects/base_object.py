from abc import ABC
from uuid import UUID, uuid4


class Base(ABC):
    """Base class for all objects within the map

    Attributes:
        id(:obj:`UUID`): unique identifer for each object
    """

    id: UUID

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.id = uuid4()

    def __repr__(self) -> str:
        return f"{self.__class__}: {self.__dict__}"

    def __str__(self) -> str:
        return f"{self.__class__}: {self.__dict__}"

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, self.__class__):
            return self.id == __o.id
        return NotImplemented

    def __ne__(self, __o: object) -> bool:
        x = self.__eq__(__o)
        if x is NotImplemented:
            return NotImplemented
        return not x

    def __hash__(self) -> int:
        return hash(tuple(sorted(self.__dict__.items())))
