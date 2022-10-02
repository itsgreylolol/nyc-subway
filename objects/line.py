from objects.base_object import BaseObject
from objects.track import Track


class Line(BaseObject):
    name: str
    current_track: Track

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def start(self) -> None:
        # TODO: Does this need an init?
        pass
