from networkx import MultiDiGraph

from enums import Division
from objects import BaseObject, Stop


class Track(MultiDiGraph, BaseObject):
    name: str
    stops: list[Stop]
    divison: Division
    direction: str

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.stops = kwargs.pop("stops", None) or []
        self.name = kwargs.pop("name", None) or ""
        self.divison = kwargs.pop("division", None) or Division.A

        self.add_nodes_from(self.stops)
        self.add_edges_from(
            [
                (stop, self.stops[index + 1])
                for index, stop in enumerate(self.stops)
                if index != (len(self.stops) - 1)
            ]
        )

        if len(self.stops) > 0:
            self.direction = f"{self.stops[0].name} to {self.stops[-1].name}"

    async def start(self) -> None:
        # TODO: Does this need an init?
        pass
