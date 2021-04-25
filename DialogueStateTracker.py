from UserActType import UserActType
from UserAct import UserAct


class DST:
    """
    Moduł odpowiedzialny za śledzenie stanu dialogu. Przechowuje informacje o tym jakie dane zostały uzyskane od użytkownika w toku prowadzonej konwersacji.
    Wejście: Akt użytkownika (rama)
    Wyjście: Reprezentacja stanu dialogu (rama)
    """

    def __init__(self):
        self.frameList = []

    def addFrame(self, frame):
        self.frameList.append(frame)

    def getFrames(self):
        return self.frameList
