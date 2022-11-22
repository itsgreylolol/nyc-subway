from __future__ import annotations

from typing import TYPE_CHECKING

from enums import Division
from objects import BaseObject

if TYPE_CHECKING:
    from objects import Track


class Line(BaseObject):
    name: str
    current_track: Track
    division: Division

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def start(self) -> None:
        # TODO: Does this need an init?
        pass
