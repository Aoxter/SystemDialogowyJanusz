from enum import Enum, unique


@unique
class SystemActType(Enum):
    WELCOME_MSG = 0
    BYE = 1
    REQMORE = 2
    AFFIRM = 3
    CONFIRM_DOMAIN = 4
    MEETING_LIST = 5
    FREE_TIME = 6
    REQUEST = 7
    NOT_UNDERSTOOD = -1
