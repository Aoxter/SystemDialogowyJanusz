from UserActType import UserActType
from ActFrame import ActFrame

class UserAct(ActFrame):
    def __init__(self, actType, actParams = None):
        if actType != None and type(actType) is not UserActType:
            raise Exception('actParams has wrong type: expected type {}, got {}'.format(type(UserActType.WELCOME_MSG), type(actType)))

        super(UserAct, self).__init__(actType, actParams)