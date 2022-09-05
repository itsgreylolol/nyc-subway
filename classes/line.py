from uuid import UUID, uuid4
from classes import Train, Stop


class Line(object):
    name: str
    trains: list[Train]
    stops: list[Stop]
    id: UUID

    def __init__(self, name: str, trains: list[Train], stops: list[Stop]) -> None:
        self.trains = trains
        self.name = name
        self.stops = stops

        self.id = uuid4()
