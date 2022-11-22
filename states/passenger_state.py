from __future__ import annotations

from asyncio import sleep
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from objects import Passenger, Stop, Train


class PassengerState(object):
    _passenger: Passenger

    @property
    def passenger(self) -> Passenger:
        return self._passenger

    @passenger.setter
    def passenger(self, passenger: Passenger) -> None:
        self._passenger = passenger

    async def waiting(self, stop: Stop) -> PassengerState:
        # note: this should be a minimum wait of time to transfer lines (edge weight)
        # TODO: implement minimum waiting time
        # TODO: implement global timer for passenger trip
        train = None  # TODO: implement logic for finding train boarded
        self.passenger.state = await self.boarding(stop, train)
        return self

    async def boarding(self, stop: Stop, train: Train) -> PassengerState:
        # TODO: implement global boarding time
        self.passenger.state = await self.in_transit(train)
        return self

    async def in_transit(self, train: Train) -> PassengerState:
        # this may just end up being a pass through?
        # may need logic for events during transit
        # but time in transit is handled by the train
        stop = None  # TODO: need logic for next stop
        while train.state != train.state.stopped:
            await sleep(0.01)

        # TODO: implement transfer logic
        if stop != self.passenger.dest:
            self.passenger.state = await self.in_transit(train)

        self.passenger.state = await self.deboarding(stop)
        return self

    async def deboarding(self, stop: Stop) -> PassengerState:
        # TODO: implement transfer logic
        if stop != self.passenger.dest:
            self.passenger.state = await self.waiting(stop)

        return self

        # TODO: stop passenger travel timer
        # TODO: log metrics
