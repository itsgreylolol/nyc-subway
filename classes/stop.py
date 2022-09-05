from uuid import UUID, uuid4
from classes import Passenger


class Stop(object):
    name: str
    time_to_stop: int
    is_last: bool
    id: UUID
    passengers: list[Passenger]

    def __init__(
        self,
        name: str,
        time_to_stop: int,
        is_last: bool = False,
    ) -> None:
        self.name = name
        self.time_to_stop = time_to_stop
        self.is_last = is_last

        self.id = uuid4()
        self.passengers = []
