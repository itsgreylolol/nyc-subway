from datetime import datetime
from itertools import chain

from matplotlib import pyplot as plt
from networkx import Graph, compose_all, draw_networkx
from pandas import read_csv

from objects import Passenger, Stop, Track
from util import PassengerFactory

factory = PassengerFactory()


class Simulation(object):
    map: Graph
    stops: list[Stop]
    passengers: list[Passenger]

    def __init__(self, start_date: datetime, end_date: datetime) -> None:
        self.map = self._get_map()
        self.passengers = factory.create_passengers(self.map, start_date, end_date)
        draw_networkx(self.map, node_size=10, with_labels=False)
        plt.savefig("./cache/map.png")

    def _get_map(self) -> Graph:
        data = read_csv("./data/stops.csv")
        data["LINES"] = data["LINE"].apply(lambda x: x.split("-"))
        self.stops = data.apply(
            lambda x: Stop(x["NAME"], 0, x["LINES"]), axis=1
        ).tolist()

        line_names = set(chain.from_iterable(data["LINES"]))
        temp_tracks = [
            self._create_track(x, [stop for stop in self.stops if x in stop.tracks])
            for x in line_names
        ]
        tracks = [item for sublist in temp_tracks for item in sublist]

        # TODO: Track naming convention and mapping to lines
        # TODO: Lines https://en.wikipedia.org/wiki/New_York_City_Subway_rolling_stock
        return compose_all(tracks)

    @staticmethod
    def _create_track(name: str, stops: list[Stop]) -> tuple[Track, Track]:
        first = Track(name=name, stops=stops)
        stops.reverse()
        second = Track(name=name, stops=stops)

        return first, second

    async def run(self) -> None:
        # TODO: implement gather
        #       https://docs.python.org/3/library/asyncio-task.html#id6
        pass
