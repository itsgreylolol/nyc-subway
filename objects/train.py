import logging

from objects.base_object import BaseObject
from objects.passenger import Passenger
from objects.stop import Stop
from objects.track import Track
from states.train_state import TrainState


class Train(BaseObject):
    track: Track
    max_passengers: int
    passengers: list[Passenger]
    current_stop: Stop
    open_places: int
    on_board: int
    _state: TrainState

    def __init__(
        self, track: Track, max_passengers: int, state: TrainState, *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.track = track
        self.max_passengers = max_passengers
        self.state = state

        self.passengers = []
        self.current_stop = self.track.stops[0]

    @property
    def open_places(self) -> int:
        return self.size - len(self.passengers)

    @property
    def on_board(self) -> int:
        return len(self.passengers)

    @property
    def state(self) -> TrainState:
        logging.info(f"Train is {type(self._state).__name__}")
        return self._state

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

    async def start(self) -> None:
        # TODO: implement anything to be done before start
        self._state.stopped(self.current_stop)
