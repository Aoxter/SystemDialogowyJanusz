from enum import Enum, unique


@unique
class UserActType(Enum):
    WELCOME_MSG = 0
    REQUEST = 1
    BYE = 2
    INVALID = -1
