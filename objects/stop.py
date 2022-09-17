from __future__ import annotations

from uuid import UUID, uuid4
from typing import TYPE_CHECKING

from objects import Base

if TYPE_CHECKING:
    from objects import Train, Passenger


class Stop(Base):
    name: str
    time_to_stop: int
    lines: list[str]
    id: UUID
    passengers: list[Passenger]
    current_train: Train

    def __init__(self, name: str, time_to_stop: int, lines: list[str]) -> None:
        self.name = name
        self.time_to_stop = time_to_stop
        self.lines = lines

        self.id = uuid4()
        self.passengers = []
        self.current_train = None
