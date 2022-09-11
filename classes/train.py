import copy
import time
import logging

from uuid import UUID, uuid4

from classes import Line, Stop, Passenger
from states.train_state import TrainState


class Train(object):
    line: Line
    max_passengers: int
    passengers: list[Passenger]
    current_stop: Stop
    id: UUID
    open_places: int
    on_board: int
    _state: TrainState

    def __init__(self, line: Line, max_passengers: int, state: TrainState) -> None:
        self.line = line
        self.max_passengers = max_passengers
        self.state = state

        self.passengers = []
        self.current_stop = self.line.stops[0]
        self.id = uuid4()

    @property
    def open_places(self) -> int:
        return self.size - len(self.passengers)

    @property
    def on_board(self) -> int:
        return len(self.passengers)

    @property
    def state(self) -> None:
        logging.info(f"Train is {type(self._state).__name__}")

    @state.setter
    def state(self, state: TrainState) -> None:
        self._state = state
        self._state.train = self

    def arriving(self, stop: Stop) -> None:
        self._state.arriving(stop)

    def stopped(self, stop: Stop) -> None:
        self._state.stopped(stop)

    def departing(self, stop: Stop) -> None:
        self._state.departing(stop)

    def in_transit(self) -> None:
        self._state.in_transit()

    def arrive(self, stop: Stop) -> list[Passenger]:
        stop.current_train = self
        self.current_stop = stop
        boarding_passengers = [
            passenger
            for passenger in stop.passengers
            if passenger.current.id == stop.id
        ]
        self.passengers.extend(boarding_passengers)

        out_passengers = []

        if stop.is_last:
            out_passengers = self.empty()
        else:
            out_passengers = [
                passenger
                for passenger in self.passengers
                if passenger.dest.id == stop.id
            ]

            for passenger in out_passengers:
                self.passengers.remove(passenger)

        # TODO: add logic to account for long running code above this
        time.sleep(stop.time_to_stop)

        stop.current_train = None
        self.depart()
        return out_passengers

    async def depart(self) -> None:
        next_stop_index = self.line.stops.index(self.current_stop)

        self.current_stop = None

    def empty(self) -> list[Passenger]:
        out_passengers = copy.deepcopy(self.passengers)

        self.passengers = []

        return out_passengers
