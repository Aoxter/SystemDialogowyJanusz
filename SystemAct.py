from SystemActType import SystemActType
from ActFrame import ActFrame

class SystemAct(ActFrame):
    def __init__(self, actType, actParams = None):
        if actType != None and type(actType) is not SystemActType:
            raise Exception('actParams has wrong type: expected type {}, got {}'.format(type(SystemActType.WELCOME_MSG), type(actType)))

        super(SystemAct, self).__init__(actType, actParams)

    def isDialogFinished(self):
        return self.getActType() == SystemActType.BYE
