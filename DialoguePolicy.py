from SystemAct import SystemAct
from UserActType import UserActType
from SystemActType import SystemActType
from collections import defaultdict


class DP:
    """
    Moduł decydujący o wyborze kolejnego aktu, który ma podjąć system prowadząc rozmowę.
    Wejście: Reprezentacja stanu dialogu (rama)
    Wyjście: Akt systemu (rama)
    """

    def __init__(self):
        self.results = []

    def chooseTactic(self, current_frame) -> SystemAct:
        #userAct = frameList[-1]
        if current_frame.getActType() == UserActType.HELLO:
            return  SystemAct(SystemActType.WELCOME_MSG)
        elif current_frame.getActType() == UserActType.BYE:
            return SystemAct(SystemActType.BYE)
        elif current_frame.getActType() == UserActType.CONFIRM:
            # Czy napewno zawsze po Confirm jest Affirm?
            return SystemAct(SystemActType.AFFIRM)
        elif current_frame.getActType() == UserActType.NEGATE:
            # TODO rozpoznanie czy ma się już komplet danych
            # Affirm (gdy ma się wszystkie potrzebne zdanie)
            # Request (gdy potrzeba się dopytać dalej)
            # Bye (gdy to odp na REQMORE)
            return SystemAct(SystemActType.AFFIRM)
        elif current_frame.getActType() == UserActType.THANKYOU:
            return SystemAct(SystemActType.REQMORE)
        elif current_frame.getActType() == UserActType.INFORM:
            # TODO najczęściej chyba AFFIRM, CONFIRM_DOMAIN i REQUEST
            return SystemAct(SystemActType.REQUEST)
        elif current_frame.getActType() == UserActType.CREATE_MEETING:
            # TODO najczęściej chyba CONFIRM_DOMAIN i REQUEST
            return SystemAct(SystemActType.REQUEST)
        elif current_frame.getActType() == UserActType.UPDATE_MEETING:
            # TODO rozpoznanie czy ma się już komplet danych jak nie to REQUEST jak tak to CONFIRM_DOMAIN
            return SystemAct(SystemActType.REQUEST)
        elif current_frame.getActType() == UserActType.CANCEL_MEETING:
            # TODO rozpoznanie czy ma się już komplet danych jak nie to REQUEST jak tak to CONFIRM_DOMAIN
            return SystemAct(SystemActType.REQUEST)
        elif current_frame.getActType() == UserActType.MEETING_LIST:
            return SystemAct(SystemActType.INFORM, ["meeting_list"])
        elif current_frame.getActType() == UserActType.FREE_TIME:
            return SystemAct(SystemActType.INFORM, ["freetime"])
        elif current_frame.getActType() == UserActType.INVALID:
            return SystemAct(SystemActType.NOT_UNDERSTOOD)
        else:
            return SystemAct(SystemActType.INFORM,['name'])
