import copy

from itertools import chain

import pandas as pd

from networkx import Graph, MultiDiGraph, compose_all

from objects import Line, Stop


class Simulation(object):
    map: Graph

    def __init__(self) -> None:
        self.map = self._get_map()

    def _get_map(self) -> Graph:
        data = pd.read_csv("./data/stops.csv")
        data["LINES"] = data["LINE"].apply(lambda x: x.split("-"))
        stops: list[Stop] = list(
            data.apply(lambda x: Stop(x["NAME"], 0, x["LINES"]), axis=1)
        )
        line_names = set(chain.from_iterable(data["LINES"]))
        lines = [
            Line(x, [stop for stop in stops if x in stop.lines]) for x in line_names
        ]
        graphs = [self._create_graph(x) for x in lines]
        return compose_all(graphs)

    def _create_graph(self, line: Line) -> MultiDiGraph:
        graph = MultiDiGraph(name=line.name)
        stops = copy.deepcopy(line.stops)

        graph.add_nodes_from(stops)
        graph.add_edges_from(
            [
                (stop, stops[index + 1])
                for index, stop in enumerate(stops)
                if index != (len(stops) - 1)
            ]
        )
        stops.reverse()

        graph.add_edges_from(
            [
                (stop, stops[index + 1])
                for index, stop in enumerate(stops)
                if index != (len(stops) - 1)
            ]
        )

        return graph

    def run(self) -> None:
        # placeholder
        pass
