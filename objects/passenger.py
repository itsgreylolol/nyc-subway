from __future__ import annotations

from asyncio import sleep
from logging import info
from typing import TYPE_CHECKING

from enums import PassengerState
from objects import BaseObject

if TYPE_CHECKING:
    from objects import Stop, Train
    from util import Timer


class Passenger(BaseObject):
    source: Stop
    dest: Stop
    current: Stop
    path: list[Stop]
    timer: Timer
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
        assert isinstance(state, PassengerState)
        self._state = state

    def waiting(self, stop: Stop) -> None:
        # note: this should be a minimum wait of time to transfer lines (edge weight)
        # TODO: implement minimum waiting time

        self.state = PassengerState.WAITING
        train = None  # TODO: implement logic for finding train boarded
        self.run(self.boarding, {"stop": stop, "train": train})

    def boarding(self, stop: Stop, train: Train) -> None:
        # TODO: implement global boarding time
        self.state = PassengerState.BOARDING
        self.run(self.in_transit, {"train": train})

    async def in_transit(self, train: Train) -> None:
        # this may just end up being a pass through?
        # may need logic for events during transit
        # but time in transit is handled by the train

        self.state = PassengerState.IN_TRANSIT
        stop = None  # TODO: need logic for next stop
        while train.state != train.state.STOPPED:
            await sleep(1)

        # TODO: implement transfer logic
        if stop != self.dest:
            self.run(self.in_transit, {"train": train})

        self.run(self.deboarding, {"stop": stop})

    def deboarding(self, stop: Stop) -> None:
        # TODO: implement transfer logic
        self.state = PassengerState.DEBOARDING

        if stop != self.dest:
            self.run(self.waiting, {"stop": stop})
        else:
            self.exiting()

    def exiting(self) -> None:
        # TODO: log metrics
        self.state = PassengerState.EXITING
        travel_time = self.timer.stop()
        del self

    async def start(self) -> None:
        self.timer.start()
        self.run(self.waiting, {"stop": self.current})
