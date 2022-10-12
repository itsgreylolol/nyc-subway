from __future__ import annotations

from logging import info
from typing import TYPE_CHECKING

from objects.base_object import BaseObject

if TYPE_CHECKING:
    from objects.stop import Stop
    from objects.train import Train
    from states.passenger_state import PassengerState


class Passenger(BaseObject):
    source: Stop
    dest: Stop
    current: Stop
    path: list[Stop]
    _state: PassengerState

    def __init__(
        self,
        source: Stop,
        dest: Stop,
        path: list[Stop],
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.source = source
        self.dest = dest
        self.path = path

        self.current = source

    @property
    def state(self) -> PassengerState:
        info(f"Passenger is {type(self._state).__name__}")
        return self._state

    @state.setter
    def state(self, state: PassengerState) -> None:
        self._state = state
        self._state.passenger = self

    def waiting(self, stop: Stop) -> None:
        self._state.waiting(stop)

    def boarding(self, stop: Stop, train: Train) -> None:
        self._state.boarding(stop, train)

    async def in_transit(self, train: Train) -> None:
        await self._state.in_transit(train)

    def deboarding(self, stop: Stop) -> None:
        self._state.deboarding(stop)

    async def start(self) -> None:
        # TODO: init timer
        self._state.waiting(self.source)
