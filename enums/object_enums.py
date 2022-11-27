from enum import auto

from enums.base_enum import BaseEnum


class Division(BaseEnum):
    A = auto()
    B = auto()
    S = auto()


class PassengerState(BaseEnum):
    ENTERING = auto()
    WAITING = auto()
    BOARDING = auto()
    IN_TRANSIT = auto()
    DEBOARDING = auto()
    EXITING = auto()


class TrainState(BaseEnum):
    ARRIVING = auto()
    STOPPED = auto()
    DEPARTING = auto()
    IN_TRANSIT = auto()
