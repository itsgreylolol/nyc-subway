class Base(object):
    def __init__(self) -> None:
        super().__init__()

    def __repr__(self) -> str:
        return f"{self.__class__}: {self.__dict__}"

    def __str__(self) -> str:
        return f"{self.__class__}: {self.__dict__}"
