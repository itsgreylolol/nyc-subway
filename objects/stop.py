from __future__ import annotations

from typing import TYPE_CHECKING

from objects.base_object import BaseObject

if TYPE_CHECKING:
    from objects.passenger import Passenger
    from objects.train import Train


class Stop(BaseObject):
    name: str
    time_to_stop: int
    tracks: list[str]
    passengers: list[Passenger]
    current_train: Train

    def __init__(
        self, name: str, time_to_stop: int, tracks: list[str], *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.name = name
        self.time_to_stop = time_to_stop
        self.tracks = tracks

        self.passengers = []
        self.current_train = None
