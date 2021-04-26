from enum import Enum, unique


@unique
class SystemActType(Enum):
    WELCOME_MSG = 0
    INFORM = 1
    BYE = 2
    NOT_UNDERSTOOD = -1
