import time

from objects.stop import Stop
from objects.train import Train
from objects.passenger import Passenger


class PassengerState(object):
    _passenger: Passenger

    @property
    def passenger(self) -> Passenger:
        return self._passenger

    @passenger.setter
    def passenger(self, passenger: Passenger) -> None:
        self._passenger = passenger

    def waiting(self, stop: Stop) -> None:
        # note: this should be a minimum wait of time to transfer lines (edge weight)
        # TODO: implement minimum waiting time
        # TODO: implement global timer for passenger trip
        train = None  # TODO: implement logic for finding train boarded
        self.passenger.state = self.boarding(stop, train)

    def boarding(self, stop: Stop, train: Train) -> None:
        # TODO: implement global boarding time
        self.passenger.state = self.in_transit(train)

    def in_transit(self, train: Train) -> None:
        # this may just end up being a pass through?
        # may need logic for events during transit
        # but time in transit is handled by the train
        stop = None  # TODO: need logic for next stop
        while train.state != train.state.stopped:
            time.sleep(0.01)

        # TODO: implement transfer logic
        if stop != self.passenger.dest:
            self.passenger.state = self.in_transit(train)

        self.passenger.state = self.deboarding(stop)

    def deboarding(self, stop: Stop) -> None:
        # TODO: implement transfer logic
        if stop != self.passenger.dest:
            self.passenger.state = self.waiting(stop)

        # TODO: stop passenger travel timer
        # TODO: log metrics
