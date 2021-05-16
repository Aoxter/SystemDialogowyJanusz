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
        if userAct.getActType() == UserActType.HELLO:
            return  SystemAct(SystemActType.WELCOME_MSG)
        elif userAct.getActType() == UserActType.BYE:
            return SystemAct(SystemActType.BYE)
        elif userAct.getActType() == UserActType.INVALID:
            return SystemAct(SystemActType.NOT_UNDERSTOOD)
        else:
            return SystemAct(SystemActType.INFORM,['name'])
