from __future__ import annotations

from typing import TYPE_CHECKING

from objects.base_object import Base

if TYPE_CHECKING:
    from objects.passenger import Passenger
    from objects.train import Train


class Stop(Base):
    name: str
    time_to_stop: int
    lines: list[str]
    passengers: list[Passenger]
    current_train: Train

    def __init__(
        self, name: str, time_to_stop: int, lines: list[str], *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.name = name
        self.time_to_stop = time_to_stop
        self.lines = lines

        self.passengers = []
        self.current_train = None
