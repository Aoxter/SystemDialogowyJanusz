class NLG:
    """
    Moduł, który tworzy reprezentację tekstową aktu systemowego wybranego przez taktykę dialogu.
    Wejście: Akt systemu (rama)
    Wyjście: Tekst
    """

    def __init__(self):
        pass

    def toText(self, systemAct):
        if systemAct == [1]:
            return "Nie rozumiem o czym mówisz."
        if systemAct == [2]:
            return "Do widzenia."
        else:
            return "Witaj, nazywam się Janusz."
