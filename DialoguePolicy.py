from SystemAct import SystemAct
from UserActType import UserActType
from SystemActType import SystemActType


class DP:
    """
    Moduł decydujący o wyborze kolejnego aktu, który ma podjąć system prowadząc rozmowę.
    Wejście: Reprezentacja stanu dialogu (rama)
    Wyjście: Akt systemu (rama)
    """

    def __init__(self):
        pass

    def chooseTactic(self, frameList=None) -> SystemAct:
        userAct = frameList[-1]
        if userAct.getActType() == UserActType.WELCOME_MSG:
            return  SystemAct(SystemActType.WELCOME_MSG)
        if userAct.getActType() == UserActType.REQUEST:
            if "name" in userAct.getActParams():
                return SystemAct(SystemActType.INFORM,['name'])
        if userAct.getActType() == UserActType.BYE:
            return SystemAct(SystemActType.BYE)
        if userAct.getActType() == UserActType.INVALID:
            return SystemAct(SystemActType.NOT_UNDERSTOOD)
        raise Exception("UserAct:{} not recognized".format(userAct))
