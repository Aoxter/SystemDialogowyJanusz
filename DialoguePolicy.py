from UserActType import UserActType
from UserAct import UserAct


class DP:
    """
    Moduł decydujący o wyborze kolejnego aktu, który ma podjąć system prowadząc rozmowę.
    Wejście: Reprezentacja stanu dialogu (rama)
    Wyjście: Akt systemu (rama)
    """

    def __init__(self):
        pass

    def chooseTactic(self, frameList=None):
        if frameList[-1].getActType() is UserActType.INVALID:
            systemAct = [1]
            return systemAct
        elif frameList[-1].getActType() is UserActType.BYE:
            systemAct = [2]
            return systemAct
        else:
            systemAct = [0]
            return systemAct
