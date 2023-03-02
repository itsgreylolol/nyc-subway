from itertools import chain

import pandas as pd
from matplotlib import pyplot as plt
from networkx import Graph, compose_all, draw

from objects.stop import Stop
from objects.track import Track


class Simulation(object):
    map: Graph

    def __init__(self) -> None:
        self.map = self._get_map()
        draw(self.map)
        plt.savefig("./cache/map.png")

    def _get_map(self) -> Graph:
        data = pd.read_csv("./data/stops.csv")
        data["LINES"] = data["LINE"].apply(lambda x: x.split("-"))
        stops: list[Stop] = list(
            data.apply(lambda x: Stop(x["NAME"], 0, x["LINES"]), axis=1)
        )
        line_names = set(chain.from_iterable(data["LINES"]))
        tracks = [
            Track(name=x, stops=[stop for stop in stops if x in stop.tracks])
            for x in line_names
        ]

        # TODO: Track naming convention and mapping to lines
        # TODO: Lines https://en.wikipedia.org/wiki/New_York_City_Subway_rolling_stock
        return compose_all(tracks)

    async def run(self) -> None:
        # TODO: implement gather
        #       https://docs.python.org/3/library/asyncio-task.html#id6
        pass
