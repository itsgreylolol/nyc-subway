import logging

from networkx import Graph, compose_all

from objects.line import Line
from objects.stop import Stop
from util.data_util import get_turnstile_data


class Simulation(object):
    map: Graph

    def __init__(self) -> None:
        data = get_turnstile_data()
        groups = data.groupby("STATION")["LINENAME"].agg(list).to_frame().reset_index()
        groups["LINENAME"] = groups["LINENAME"].apply(
            lambda x: list({l for word in x for l in word})
        )
        stops: list[Stop] = list(
            groups.apply(lambda x: Stop(x["STATION"], 0, x["LINENAME"]))
        )
        line_names = data["LINENAME"].apply(
            lambda x: list({l for word in x for l in word})
        )
        lines = line_names.apply(
            lambda x: Line(x, [stop for stop in stops if x in stop.lines])
        )
        logging.info(lines)

    def run(self) -> None:
        # placeholder
        pass
