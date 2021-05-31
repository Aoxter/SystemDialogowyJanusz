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

    def __init__(self, dst):
        self.DST = dst

    def chooseTactic(self) -> SystemAct:
        dialogue_state, last_user_act, last_system_act = self.DST.get_dialogue_state()
        slots = self.DST.get_dialogue_slots()
        # stan dodawania spotkania
        if dialogue_state == UserActType.CREATE_MEETING:
            if not last_system_act:
                if 'date' not in slots:
                    return SystemAct(SystemActType.REQUEST, ['date'])
                elif 'time' not in slots:
                    return SystemAct(SystemActType.REQUEST, ['time'])
                elif 'place' not in slots:
                    return SystemAct(SystemActType.REQUEST, ['place'])
                elif 'description' not in slots:
                    return SystemAct(SystemActType.REQUEST, ['description'])
                elif 'participants' not in slots:
                    return SystemAct(SystemActType.REQUEST, ['participants'])
                else:
                    return SystemAct(SystemActType.CONFIRM_DOMAIN, slots)
            elif last_system_act.getActType() == SystemActType.REQUEST:
                if last_user_act == UserActType.NEGATE:
                    slot_type = last_system_act.getActParams()[0]
                    if slot_type not in ['date', 'time']:
                        self.DST.insert_empty_slot(slot_type)
                if 'date' not in slots:
                    return SystemAct(SystemActType.REQUEST, ['date'])
                elif 'time' not in slots:
                    return SystemAct(SystemActType.REQUEST, ['time'])
                elif 'place' not in slots:
                    return SystemAct(SystemActType.REQUEST, ['place'])
                elif 'description' not in slots:
                    return SystemAct(SystemActType.REQUEST, ['description'])
                elif 'participants' not in slots:
                    return SystemAct(SystemActType.REQUEST, ['participants'])
                else:
                    return SystemAct(SystemActType.CONFIRM_DOMAIN, slots)
            elif last_system_act.getActType() == SystemActType.CONFIRM_DOMAIN:
                if last_user_act == UserActType.CONFIRM:
                    system_act = SystemAct(SystemActType.AFFIRM, ['create_meeting'])
                    # implementacja wpisywanie spotkania do bazy
                    self.DST.clear()
                    return system_act
                elif last_user_act == UserActType.NEGATE:
                    self.DST.clear()
                    return SystemAct(SystemActType.REQMORE, [])
            else:
                return SystemAct(SystemActType.NOT_UNDERSTOOD, [])
        # stan edycji spotkania
        elif dialogue_state == UserActType.UPDATE_MEETING:
            meeting_to_update = False
            if not last_system_act:
                if 'date' not in slots:
                    return SystemAct(SystemActType.REQUEST, ['date'])
                elif 'time' not in slots:
                    return SystemAct(SystemActType.REQUEST, ['time'])
                else:
                    # implementacja wyszukiwania odpowiedniego spotkania w bazie
                    return SystemAct(SystemActType.CONFIRM_DOMAIN, ['meeting_to_update'])
            elif last_system_act.getActType() == SystemActType.REQUEST:
                if not meeting_to_update:    
                    if 'date' not in slots:
                        return SystemAct(SystemActType.REQUEST, ['date'])
                    elif 'time' not in slots:
                        return SystemAct(SystemActType.REQUEST, ['time'])
                    else:
                        # implementacja wyszukiwania odpowiedniego spotkania w bazie
                        return SystemAct(SystemActType.CONFIRM_DOMAIN, ['meeting_to_update'])
                else:
                    if last_user_act == UserActType.NEGATE:
                        slot_type = last_system_act.getActParams()[0]
                        if slot_type not in ['date', 'time']:
                            self.DST.insert_empty_slot(slot_type)
                        if 'date' not in slots:
                            return SystemAct(SystemActType.REQUEST, ['date'])
                        elif 'time' not in slots:
                            return SystemAct(SystemActType.REQUEST, ['time'])
                        elif 'place' not in slots:
                            return SystemAct(SystemActType.REQUEST, ['place'])
                        elif 'description' not in slots:
                            return SystemAct(SystemActType.REQUEST, ['description'])
                        elif 'participants' not in slots:
                            return SystemAct(SystemActType.REQUEST, ['participants'])
                        else:
                            return SystemAct(SystemActType.CONFIRM_DOMAIN, slots)
            elif last_system_act.getActType() == SystemActType.CONFIRM_DOMAIN:
                if meeting_to_update:
                    if last_user_act == UserActType.CONFIRM:
                        meeting_to_update = False
                        self.DST.clear()
                        return SystemAct(SystemActType.AFFIRM, ['update_meeting'])
                    elif last_user_act == UserActType.NEGATE:
                        self.DST.clear()
                        return SystemAct(SystemActType.REQMORE, [])
                    meeting_to_update = False
                if not meeting_to_update:
                    if last_user_act == UserActType.CONFIRM:
                        meeting_to_update = True
                        self.DST.clear_slots()
                        return SystemAct(SystemActType.REQUEST, ['date'])
                    elif last_user_act == UserActType.NEGATE:
                        self.DST.clear()
                        return SystemAct(SystemActType.REQMORE, [])
            else:
                return SystemAct(SystemActType.NOT_UNDERSTOOD, [])
        # stan anulowania spotkania
        elif dialogue_state == UserActType.CANCEL_MEETING:
            if not last_system_act:
                if 'date' not in slots:
                    return SystemAct(SystemActType.REQUEST, ['date'])
                elif 'time' not in slots:
                    return SystemAct(SystemActType.REQUEST, ['time'])
                else:
                    # implementacja wyszukiwania odpowiedniego spotkania w bazie
                    return SystemAct(SystemActType.CONFIRM_DOMAIN, ['cancel_meeting'])
            elif last_system_act.getActType() == SystemActType.REQUEST:    
                if 'date' not in slots:
                    return SystemAct(SystemActType.REQUEST, ['date'])
                elif 'time' not in slots:
                    return SystemAct(SystemActType.REQUEST, ['time'])
                else:
                    # implementacja wyszukiwania odpowiedniego spotkania w bazie
                    return SystemAct(SystemActType.CONFIRM_DOMAIN, ['cancel_meeting'])
            elif last_system_act.getActType() == SystemActType.CONFIRM_DOMAIN:
                if last_user_act == UserActType.CONFIRM:
                    system_act = SystemAct(SystemActType.AFFIRM, ['cancel_meeting'])
                    # implementacja usuwania spotkania z bazy
                    self.DST.clear()
                    return system_act
                elif last_user_act == UserActType.NEGATE:
                    self.DST.clear()
                    return SystemAct(SystemActType.REQMORE, [])
            else:
                return SystemAct(SystemActType.NOT_UNDERSTOOD, [])
        # stan prośby o listę spotkań
        elif dialogue_state == UserActType.MEETING_LIST:
            if last_user_act == UserActType.NEGATE:
                self.DST.clear()
                return SystemAct(SystemActType.REQMORE, [])
            else:
                if 'date' in slots:
                    system_act = SystemAct(SystemActType.MEETING_LIST, slots)
                    self.DST.clear()
                    return system_act
                else:
                    return SystemAct(SystemActType.REQUEST, ['date'])
        # stan prośby o czas wolny
        elif dialogue_state == UserActType.FREE_TIME:
            if last_user_act == UserActType.NEGATE:
                self.DST.clear()
                return SystemAct(SystemActType.REQMORE, [])
            else:
                if 'date' in slots:
                    system_act = SystemAct(SystemActType.FREE_TIME, slots)
                    self.DST.clear()
                    return system_act
                else:
                    return SystemAct(SystemActType.REQUEST, ['date'])
        # brak określonego stanu
        else:
            if last_user_act == UserActType.HELLO:
                return SystemAct(SystemActType.WELCOME_MSG, [])
            elif last_user_act == UserActType.BYE:
                return SystemAct(SystemActType.BYE, [])
            elif last_user_act == UserActType.THANKYOU:
                return SystemAct(SystemActType.REQMORE, [])
            else:
                return SystemAct(SystemActType.NOT_UNDERSTOOD, [])
