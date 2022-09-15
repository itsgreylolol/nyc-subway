from uuid import UUID, uuid4

from networkx import MultiDiGraph

from objects.stop import Stop


class Line(MultiDiGraph):
    name: str
    id: UUID

    def __init__(self, name: str, stops: list[Stop]) -> None:
        super().__init__()
        self.add_nodes_from(stops)
        self.add_edges_from(
            [
                (stop, stops[index + 1])
                for index, stop in enumerate(stops)
                if index != (len(stops) - 1)
            ]
        )

        self.add_edges_from(
            [
                (stop, stops[index + 1])
                for index, stop in enumerate(stops.reverse())
                if index != (len(stops) - 1)
            ]
        )

        self.name = name
        self.id = uuid4()
