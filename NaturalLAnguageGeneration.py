from SystemAct import SystemAct
from SystemActType import SystemActType

class NLG:
    """
    Moduł, który tworzy reprezentację tekstową aktu systemowego wybranego przez taktykę dialogu.
    Wejście: Akt systemu (rama)
    Wyjście: Tekst
    """

    def __init__(self):
        pass

    def toText(self, systemAct: SystemAct) -> str:
        if systemAct.getActType() == SystemActType.WELCOME_MSG:
            return "Cześć"
        if systemAct.getActType() == SystemActType.INFORM:
            if "name" in systemAct.getActParams():
                return "Nazywam się Janusz"
        if systemAct.getActType() == SystemActType.BYE:
            return "Do widzenia."
        if systemAct.getActType() == SystemActType.NOT_UNDERSTOOD:
            return "Nie rozumiem o czym mówisz."
        raise Exception("SystemAct:{} not recognized".format(systemAct))
