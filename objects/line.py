from __future__ import annotations

from uuid import UUID, uuid4
from typing import TYPE_CHECKING

from objects import Base

if TYPE_CHECKING:
    from objects import Stop


class Line(Base):
    name: str
    id: UUID
    stops: list[Stop]

    def __init__(self, name: str, stops: list[Stop]) -> None:
        super().__init__()
        self.stops = stops
        self.name = name
        self.id = uuid4()
