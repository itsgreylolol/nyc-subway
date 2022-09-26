from networkx import MultiDiGraph

from enums.object_enums import Divison
from objects.base_object import BaseObject
from objects.stop import Stop


class Track(MultiDiGraph, BaseObject):
    name: str
    stops: list[Stop]
    divison: Divison

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.stops = kwargs.pop("stops", [])
        self.name = kwargs.pop("name", None)
        self.divison = kwargs.pop("division", None)

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
