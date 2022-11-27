from __future__ import annotations

from typing import TYPE_CHECKING

from matplotlib import pyplot as plt
from networkx import draw_networkx
from pandas import DataFrame

if TYPE_CHECKING:
    from tasks.sim import Simulation


class Debug:
    sim: Simulation

    def __init__(
        self, sim: Simulation, draw_map: bool = True, output_csv: bool = True
    ) -> None:
        self.sim = sim
        if draw_map:
            self.draw_map()
        if output_csv:
            self.output_csv()

    def draw_map(self) -> None:
        draw_networkx(self.sim.map, arrows=False, node_size=10, with_labels=False)
        plt.savefig("./cache/map.png")

    def output_csv(self) -> None:
        lines = [x.__dict__ for x in self.sim.lines]
        tracks = [x.__dict__ for x in self.sim.tracks]
        stops = [x.__dict__ for x in self.sim.stops]

        line_df = DataFrame.from_records(lines)
        track_df = DataFrame.from_records(tracks)
        stop_df = DataFrame.from_records(stops)

        line_df.to_csv("./cache/lines.csv")
        track_df.to_csv("./cache/tracks.csv")
        stop_df.to_csv("./cache/stops.csv")
