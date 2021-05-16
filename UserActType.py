from enum import Enum, unique


@unique
class UserActType(Enum):
    HELLO = 0
    BYE = 1
    CREATE_MEETING = 2
    CANCEL_MEETING = 3
    CHANGE_MEETING = 4
    MEETING_LIST = 5
    CONFIRM = 6
    THANKYOU = 7
    INVALID = -1
