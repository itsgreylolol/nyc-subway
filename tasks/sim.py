from networkx import compose_all

from objects import Line


class Simulation(object):
    def __init__(self, lines: list[Line]) -> None:
        self.map = compose_all(lines)

    def run() -> None:
        # placeholder
        pass
