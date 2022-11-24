from __future__ import annotations

from datetime import datetime
from random import choice

from networkx import Graph, has_path, shortest_path

from objects import Passenger, Stop
from util import DataLoader

loader = DataLoader()


class PassengerFactory(object):
    def create_passengers(
        self,
        map: Graph,
        start_date: datetime,
        end_date: datetime,
    ) -> list[Passenger]:
        # df = loader.get_turnstile_data().groupby(["STATION", "DATE", "TIME"]).agg("sum")
        # df.to_csv("./cache/groups.csv")

        # TODO: add dates for getting number of passengers to create
        passengers: list[Passenger] = []

        while len(passengers) < 10:
            source = choice(list(map.nodes))
            dest = choice(list(map.nodes))

            passenger = self._create(map, source, dest)
            if passenger:
                passengers.append(passenger)

        return passengers

    @staticmethod
    def _create(map: Graph, source: Stop, dest: Stop) -> Passenger | None:
        if has_path(map, source, dest):
            return Passenger(source, dest, shortest_path(map, source, dest))
        return None
