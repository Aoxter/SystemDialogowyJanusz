from UserActType import UserActType
from UserAct import UserAct
import re


class NLU:
    """
    Moduł odpowiedzialny za analizę tekstu. W wyniku jego działania tekstowa reprezentacja wypowiedzi użytkownika zostaje zamieniona na jej reprezentację semantyczną, najczęściej w postaci ramy.
    Wejście: Tekst
    Wyjście: Akt użytkownika (rama)
    """

    def __init__(self):
        self.__actParsePatternList = [
            (
                r"(.*)(cze(ś|s)(ć|c)|witaj|dzie(ń|n) dobry)(.*)",
                UserActType.WELCOME_MSG,
                []
            ),
            (
                r"(.*)(Jak (masz na imi(ę|e))|(si(ę|e) nazywasz))(.*)",
                UserActType.REQUEST,
                ["name"]
            ),
            (
                r"(.*)((ż|z)egnaj)|(do widzenia)|(na razie)(.*)",
                UserActType.BYE,
                []
            )
        ]

    def parseUserInput(self, text: str) -> UserAct:
        for pattern, actType, actParams in self.__actParsePatternList:
            regex = re.compile(pattern, re.IGNORECASE)
            match = regex.match(text)
            if match:
                return UserAct(actType, actParams)
        return UserAct(UserActType.INVALID)
