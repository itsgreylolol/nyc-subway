from itertools import chain

import pandas as pd
from matplotlib import pyplot as plt
from networkx import Graph, compose_all, draw

from objects.line import Line
from objects.stop import Stop


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
        lines = [
            Line(name=x, stops=[stop for stop in stops if x in stop.lines])
            for x in line_names
        ]
        return compose_all(lines)

    def run(self) -> None:
        # placeholder
        pass
