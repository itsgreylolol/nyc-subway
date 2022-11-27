from __future__ import annotations

from typing import TYPE_CHECKING

from enums import Division
from objects import BaseObject

if TYPE_CHECKING:
    from objects import Track


class Line(BaseObject):
    name: str
    tracks: list[Track]
    division: Division
    color: str

    def __init__(
        self, name: str, tracks: list[Track], division: Division, color: str
    ) -> None:
        self.name = name
        self.tracks = tracks
        self.division = division
        self.color = color

    async def start(self) -> None:
        # TODO: Does this need an init?
        pass
