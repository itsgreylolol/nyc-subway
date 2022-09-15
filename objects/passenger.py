import logging

from uuid import UUID, uuid4

from objects.stop import Stop
from objects.train import Train
from states.passenger_state import PassengerState


class Passenger(object):
    source: Stop
    dest: Stop
    current: Stop
    id: UUID
    _state: PassengerState

    def __init__(self, source: Stop, dest: Stop, state: PassengerState) -> None:
        self.source = source
        self.dest = dest
        self.state = state

        self.current = source
        self.id = uuid4()

    @property
    def state(self) -> PassengerState:
        logging.info(f"Passenger is {type(self._state).__name__}")
        return self._state

    @state.setter
    def state(self, state: PassengerState) -> None:
        self._state = state
        self._state.passenger = self

    def waiting(self, stop: Stop) -> None:
        self._state.waiting(stop)

    def boarding(self, stop: Stop, train: Train) -> None:
        self._state.boarding(stop, train)

    def in_transit(self, train: Train) -> None:
        self._state.in_transit(train)

    def deboarding(self, stop: Stop) -> None:
        self._state.deboarding(stop)
