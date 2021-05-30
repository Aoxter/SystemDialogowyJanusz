from enum import Enum, unique


@unique
class SystemActType(Enum):
    WELCOME_MSG = 0
    INFORM = 1
    BYE = 2
    REQUEST = 3
    INFORM = 4
    AFFIRM = 5
    CONFIRM_DOMAIN = 6
    OFFER = 7
    REQMORE = 8
    NOT_UNDERSTOOD = -1
