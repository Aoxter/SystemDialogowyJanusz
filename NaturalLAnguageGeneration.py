class NLG:
    """
    Moduł, który tworzy reprezentację tekstową aktu systemowego wybranego przez taktykę dialogu.
    Wejście: Akt systemu (rama)
    Wyjście: Tekst
    """

    def __init__(self):
        pass

    def toText(self, systemAct):
        if(systemAct == [0]):
            return "Witaj, nazywam się XXX"
        else:
            return "???"
