from enum import Enum, unique


@unique
class UserActType(Enum):
    HELLO = 0
    BYE = 1
    CONFIRM = 2
    NEGATE = 3
    THANKYOU = 4
    INFORM = 5
    CREATE_MEETING = 6
    UPDATE_MEETING = 7
    CANCEL_MEETING = 8
    MEETING_LIST = 9
    FREE_TIME = 10
    INVALID = -1
