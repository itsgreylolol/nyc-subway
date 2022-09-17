from __future__ import annotations

from networkx import MultiDiGraph

from objects.base_object import Base
from objects.stop import Stop


class Line(MultiDiGraph, Base):
    name: str
    stops: list[Stop]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.stops = kwargs.pop("stops", [])
        self.name = kwargs.pop("name", None)

        self.add_nodes_from(self.stops)
        self.add_edges_from(
            [
                (stop, self.stops[index + 1])
                for index, stop in enumerate(self.stops)
                if index != (len(self.stops) - 1)
            ]
        )
        self.stops.reverse()

        self.add_edges_from(
            [
                (stop, self.stops[index + 1])
                for index, stop in enumerate(self.stops)
                if index != (len(self.stops) - 1)
            ]
        )

        self.stops.reverse()
