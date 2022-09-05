import copy
import time
from typing import Tuple

from uuid import UUID, uuid4
from classes import Passenger, Stop, Line


class Train(object):
    line: Line
    max_passengers: int
    passengers: list[Passenger]
    current_stop: Stop
    in_transit: bool
    id: UUID
    open_places: int
    on_board: int
    is_stopped: Tuple[bool, Stop]

    def __init__(
        self,
        line: Line,
        max_passengers: int,
    ) -> None:
        self.line = line
        self.max_passengers = max_passengers

        self.passengers = []
        self.current_stop = self.line.stops[0]
        self.id = uuid4()
        self.in_transit = False

    @property
    def open_places(self) -> int:
        return self.size - len(self.passengers)

    @property
    def on_board(self) -> int:
        return len(self.passengers)

    @property
    def is_stopped(self) -> Tuple[bool, Stop]:
        return (not self.in_transit, self.current_stop)

    def arrive(self, stop: Stop) -> list[Passenger]:
        self.current_stop = stop
        self.in_transit = False
        boarding_passengers = [passenger for passenger in stop.passengers if passenger.current.id == stop.id]
        self.passengers.extend(boarding_passengers)

        out_passengers = []

        if stop.is_last:
            out_passengers = self.empty()
        else:
            out_passengers = [
                passenger for passenger in self.passengers if passenger.dest.id == stop.id
            ]

            for passenger in out_passengers:
                self.passengers.remove(passenger)

        # TODO: add logic to account for long running code above this
        time.sleep(stop.time_to_stop)

        self.in_transit = True
        self.current_stop = None
        return out_passengers

    def empty(self) -> list[Passenger]:
        out_passengers = copy.deepcopy(self.passengers)

        self.passengers = []

        return out_passengers
