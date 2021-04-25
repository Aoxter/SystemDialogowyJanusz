from UserActType import UserActType
from UserAct import UserAct
import re


class NLU:

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

    def parseUserInput(self, text):
        for pattern, actType, actParams in self.__actParsePatternList:
            regex = re.compile(pattern, re.IGNORECASE)
            match = regex.match(text)
            if match:
                return UserAct(actType, actParams)
        return UserAct(UserActType.INVALID)


if __name__ == "__main__":

    nlu = NLU()

    a = nlu.parseUserInput("czesc")
    b = nlu.parseUserInput("jak masz na imie")
    c = nlu.parseUserInput("zegnaj")

    print(a)
    print(b)
    print(c)
