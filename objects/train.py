from logging import info

from enums import TrainState
from objects import BaseObject, Passenger, Stop, Track


class Train(BaseObject):
    track: Track
    max_passengers: int
    passengers: list[Passenger]
    current_stop: Stop
    _state: TrainState

    def __init__(self, track: Track, max_passengers: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.track = track
        self.max_passengers = max_passengers

        self.passengers = []
        self.current_stop = self.track.stops[0]

    @property
    def open_places(self) -> int:
        return self.max_passengers - len(self.passengers)

    @property
    def on_board(self) -> int:
        return len(self.passengers)

    @property
    def state(self) -> TrainState:
        info(f"Train is {type(self._state).__name__}")
        return self._state

    @state.setter
    def state(self, state: TrainState) -> None:
        assert isinstance(state, TrainState)
        self._state = state

    def arriving(self, stop: Stop) -> None:
        # TODO: implement logic to ensure no train at stop
        self.state = TrainState.ARRIVING
        self.stopped(stop)

    def stopped(self, stop: Stop) -> None:
        self.state = TrainState.STOPPED
        self.departing(stop)

    def departing(self, stop: Stop) -> None:
        self.state = TrainState.DEPARTING
        self.in_transit()

    def in_transit(self) -> None:
        # TODO: implement logic to find next stop
        self.state = TrainState.IN_TRANSIT
        stop = None
        self.arriving(stop)

    async def start(self) -> None:
        # TODO: implement anything to be done before start
        self.stopped(self.current_stop)
