from datetime import datetime
from itertools import chain

from networkx import Graph, compose_all
from pandas import DataFrame, Series, read_csv

from objects import Line, Passenger, Stop, Track
from tasks.debug import Debug
from util import PassengerFactory

factory = PassengerFactory()


class Simulation(object):
    map: Graph
    stops: list[Stop]
    lines: list[Line]
    tracks: list[Track]
    passengers: list[Passenger]
    _data: DataFrame
    _created_lines: set[str]

    def __init__(self, start_date: datetime, end_date: datetime) -> None:
        self._created_lines = set()
        self.lines = []
        self._load_data()
        self.map = compose_all(self.tracks)
        self.passengers = factory.create_passengers(self.map, start_date, end_date)
        Debug(self)

    def _load_data(self) -> None:
        self._data = read_csv("./data/stops.csv")
        self._data["lines"] = self._data["line"].apply(lambda x: x.split("-"))
        self.stops: list[Stop] = self._data.apply(
            lambda x: Stop(x["name"], 0, x["lines"], x["lat"], x["long"]), axis=1
        ).tolist()

        line_names: set[str] = set(chain.from_iterable(self._data["lines"]))
        self.tracks = [
            item
            for sublist in [
                self._create_track(x, [stop for stop in self.stops if x in stop.tracks])
                for x in line_names
            ]
            for item in sublist
        ]
        self._data.apply(lambda x: self._create_lines(x), axis=1)

    def _create_lines(self, series: Series) -> None:
        for line in series["lines"]:
            if line not in self._created_lines:
                self._created_lines.add(line)
                tracks = [x for x in self.tracks if line == x.name]
                self.lines.append(
                    Line(line, tracks, series["division"], str(series["color"]))
                )

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
