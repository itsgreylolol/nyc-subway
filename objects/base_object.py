from abc import ABC, abstractmethod
from uuid import UUID, uuid4


class BaseObject(ABC):
    """Base class for all objects within the map

    Attributes:
        id(:obj:`UUID`): unique identifer for each object
    """

    id: UUID

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.id = uuid4()

    def __repr__(self) -> str:
        """Override basic logging"""
        return f"{self.__class__}: {self.__dict__}"

    def __str__(self) -> str:
        """Override basic logging"""
        return f"{self.__class__}: {self.__dict__}"

    def __eq__(self, __o: object) -> bool:
        """Override equality function to be entirely based on id"""
        if isinstance(__o, self.__class__):
            return self.id == __o.id
        return NotImplemented

    def __ne__(self, __o: object) -> bool:
        """Override equality function to be entirely based on id"""
        x = self.__eq__(__o)
        if x is NotImplemented:
            return NotImplemented
        return not x

    def __hash__(self) -> int:
        """Custom hashing, just in case"""
        return hash(self.id)

    @abstractmethod
    async def start(self) -> None:
        pass
