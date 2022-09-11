from uuid import UUID, uuid4

from objects import Stop


class Passenger(object):
    source: Stop
    dest: Stop
    current: Stop
    id: UUID

    def __init__(self, source: Stop, dest: Stop) -> None:
        self.source = source
        self.dest = dest
        self.current = source

        self.id = uuid4()
