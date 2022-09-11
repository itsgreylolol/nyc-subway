from objects import Stop, Train


class TrainState(object):
    _train: Train

    @property
    def train(self) -> Train:
        return self._train

    @train.setter
    def train(self, train: Train) -> None:
        self._train = train

    def arriving(self, stop: Stop) -> None:
        # TODO: implement state management for stop
        # TODO: implement logic to check stop for existing train
        self.train.state = self.stopped(stop)

    def stopped(self, stop: Stop) -> None:
        # TODO: implement state management for stop
        # TODO: implement boarding / de-baording logic
        self.train.state = self.departing(stop)

    def departing(self, stop: Stop) -> None:
        # TODO: implement state management for stop
        # TODO: implement way to determine transit time
        self.train.state = self.in_transit()

    def in_transit(self) -> None:
        # TODO: implement timer delay for transit time
        stop = None  # TODO: implement logic for next stop
        self.train.state = self.arriving(stop)
