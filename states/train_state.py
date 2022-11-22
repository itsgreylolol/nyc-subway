from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from objects import Stop, Train


class TrainState(object):
    _train: Train

    @property
    def train(self) -> Train:
        return self._train

    @train.setter
    def train(self, train: Train) -> None:
        assert isinstance(train, Train)
        self._train = train

    def arriving(self, stop: Stop) -> TrainState:
        # TODO: implement state management for stop
        # TODO: implement logic to check stop for existing train
        self.train.state = self.stopped(stop)
        return self

    def stopped(self, stop: Stop) -> TrainState:
        # TODO: implement state management for stop
        # TODO: implement boarding / de-baording logic
        self.train.state = self.departing(stop)
        return self

    def departing(self, stop: Stop) -> TrainState:
        # TODO: implement state management for stop
        # TODO: implement way to determine transit time
        self.train.state = self.in_transit()
        return self

    def in_transit(self) -> TrainState:
        # TODO: implement timer delay for transit time
        stop = None  # TODO: implement logic for next stop
        self.train.state = self.arriving(stop)
        return self
