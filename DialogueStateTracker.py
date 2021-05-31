from os import system
from UserActType import UserActType
from UserAct import UserAct


class DST:
    """
    Moduł odpowiedzialny za śledzenie stanu dialogu. Przechowuje informacje o tym jakie dane zostały uzyskane od użytkownika w toku prowadzonej konwersacji.
    Wejście: Akt użytkownika (rama)
    Wyjście: Reprezentacja stanu dialogu (rama)
    """

    def __init__(self):
        self.state = None
        self.last_user_act = None
        self.last_system_act = None
        self.slots = {}

    def user_update(self, frame):
        user_act = frame.getActType()
        self.last_user_act = user_act
        for slot in frame.getActParams():
            if slot[0] == 'participant':
                if 'participants' not in self.slots:
                    self.slots['participants'] = [slot[1]]
                else:
                    self.slots['participants'].append(slot[1])
            else:
                self.slots[slot[0]] = slot[1]
        if not self.state:
            if user_act in [UserActType.CREATE_MEETING, UserActType.UPDATE_MEETING, UserActType.CANCEL_MEETING, UserActType.MEETING_LIST, UserActType.FREE_TIME]:
                self.state = user_act

    def system_update(self, system_act):
        self.last_system_act = system_act

    def insert_empty_slot(self, slot_name):
        self.slots[slot_name] = None

    def clear(self):
        self.state = None
        self.slots = {}

    def clear_slots(self):
        self.slots = {}

    def get_dialogue_state(self):
        return self.state, self.last_user_act, self.last_system_act

    def get_dialogue_slots(self):
        return self.slots
