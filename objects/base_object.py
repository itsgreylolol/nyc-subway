from abc import ABC, abstractmethod
from asyncio import new_event_loop, set_event_loop
from typing import Callable
from uuid import UUID, uuid4

from util import try_except


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
        return f"{self.__class__.__name__}: {self.__dict__}"

    def __str__(self) -> str:
        """Override basic logging"""
        return f"{self.__class__.__name__}: {self.__dict__}"

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

    def __iter__(self):
        for key in self.__dict__:
            yield key, getattr(self, key)

    @abstractmethod
    async def start(self) -> None:
        pass

    @try_except
    def run(self, task: Callable, *args, **kwargs) -> None:
        loop = new_event_loop()
        set_event_loop(loop)
        new_task = loop.create_task(task(*args, **kwargs))
        loop.run_until_complete(new_task)
