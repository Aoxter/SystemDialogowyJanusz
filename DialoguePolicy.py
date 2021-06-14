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

    def __init__(self, dst, db):
        self.DST = dst
        self.DB = db
        self.meeting_to_update = False

    def chooseTactic(self) -> SystemAct:
        dialogue_state, last_user_act, last_system_act = self.DST.get_dialogue_state()
        slots = self.DST.get_dialogue_slots()
        # stan dodawania spotkania
        if dialogue_state == UserActType.CREATE_MEETING:
            if not last_system_act:
                if 'date' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['date'])
                    self.DST.system_update(system_act)
                    return system_act
                elif 'time' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['time'])
                    self.DST.system_update(system_act)
                    return system_act
                elif 'place' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['place'])
                    self.DST.system_update(system_act)
                    return system_act
                elif 'participants' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['participants'])
                    self.DST.system_update(system_act)
                    return system_act
                elif 'description' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['description'])
                    self.DST.system_update(system_act)
                    return system_act
                else:
                    system_act = SystemAct(SystemActType.CONFIRM_DOMAIN, slots)
                    self.DST.system_update(system_act)
                    return system_act
            elif last_system_act.getActType() == SystemActType.REQUEST:
                if last_user_act == UserActType.NEGATE:
                    slot_type = last_system_act.getActParams()[0]
                    if slot_type not in ['date', 'time']:
                        self.DST.insert_empty_slot(slot_type)
                if 'date' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['date'])
                    self.DST.system_update(system_act)
                    return system_act
                elif 'time' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['time'])
                    self.DST.system_update(system_act)
                    return system_act
                elif 'place' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['place'])
                    self.DST.system_update(system_act)
                    return system_act
                elif 'participants' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['participants'])
                    self.DST.system_update(system_act)
                    return system_act
                elif 'description' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['description'])
                    self.DST.system_update(system_act)
                    return system_act
                else:
                    # TODO sprawdzanie czy spotkanie nie koliduje
                    system_act = SystemAct(SystemActType.CONFIRM_DOMAIN, slots)
                    self.DST.system_update(system_act)
                    return system_act
            elif last_system_act.getActType() == SystemActType.CONFIRM_DOMAIN:
                if last_user_act == UserActType.CONFIRM:
                    system_act = SystemAct(SystemActType.AFFIRM, ['create_meeting'])
                    # implementacja wpisywanie spotkania do bazy
                    self.DB.create_meeting(slots)
                    self.DST.clear()
                    return system_act
                elif last_user_act == UserActType.NEGATE:
                    self.DST.clear()
                    return SystemAct(SystemActType.REQMORE, ['create_meeting'])
            else:
                return SystemAct(SystemActType.NOT_UNDERSTOOD, [])
        # stan edycji spotkania
        elif dialogue_state == UserActType.UPDATE_MEETING:
            if not last_system_act:
                if 'date' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['date'])
                    self.DST.system_update(system_act)
                    return system_act
                elif 'time' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['time'])
                    self.DST.system_update(system_act)
                    return system_act
                else:
                    # implementacja wyszukiwania odpowiedniego spotkania w bazie
                    return SystemAct(SystemActType.CONFIRM_DOMAIN, ['meeting_to_update'])
            elif last_system_act.getActType() == SystemActType.REQUEST:
                if not self.meeting_to_update:    
                    if 'date' not in slots:
                        system_act = SystemAct(SystemActType.REQUEST, ['date'])
                        self.DST.system_update(system_act)
                        return system_act
                    elif 'time' not in slots:
                        system_act = SystemAct(SystemActType.REQUEST, ['time'])
                        self.DST.system_update(system_act)
                        return system_act
                    else:
                        # implementacja wyszukiwania odpowiedniego spotkania w bazie
                        system_act = SystemAct(SystemActType.CONFIRM_DOMAIN, ['meeting_to_update'])
                        self.DST.system_update(system_act)
                        return system_act
                else:
                    if last_user_act == UserActType.NEGATE:
                        slot_type = last_system_act.getActParams()[0]
                        self.DST.insert_empty_slot(slot_type)
                        if 'date' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['date'])
                            self.DST.system_update(system_act)
                            return system_act
                        elif 'time' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['time'])
                            self.DST.system_update(system_act)
                            return system_act
                        elif 'place' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['place'])
                            self.DST.system_update(system_act)
                            return system_act
                        elif 'description' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['description'])
                            self.DST.system_update(system_act)
                            return system_act
                        elif 'participants' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['participants'])
                            self.DST.system_update(system_act)
                            return system_act
                        else:
                            system_act = SystemAct(SystemActType.CONFIRM_DOMAIN, slots)
                            self.DST.system_update(system_act)
                            return system_act
                    else:
                        if 'date' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['date'])
                            self.DST.system_update(system_act)
                            return system_act
                        elif 'time' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['time'])
                            self.DST.system_update(system_act)
                            return system_act
                        elif 'place' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['place'])
                            self.DST.system_update(system_act)
                            return system_act
                        elif 'description' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['description'])
                            self.DST.system_update(system_act)
                            return system_act
                        elif 'participants' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['participants'])
                            self.DST.system_update(system_act)
                            return system_act
                        else:
                            system_act = SystemAct(SystemActType.CONFIRM_DOMAIN, slots)
                            self.DST.system_update(system_act)
                            return system_act
            elif last_system_act.getActType() == SystemActType.CONFIRM_DOMAIN:
                if self.meeting_to_update:
                    if last_user_act == UserActType.CONFIRM:
                        self.DST.clear()
                        return SystemAct(SystemActType.AFFIRM, ['update_meeting'])
                    elif last_user_act == UserActType.NEGATE:
                        self.DST.clear()
                        return SystemAct(SystemActType.REQMORE, ['meeting_to_update'])
                    self.meeting_to_update = False
                if not self.meeting_to_update:
                    if last_user_act == UserActType.CONFIRM:
                        self.meeting_to_update = True
                        self.DST.clear_slots()
                        system_act = SystemAct(SystemActType.REQUEST, ['date'])
                        self.DST.system_update(system_act)
                        return system_act
                    elif last_user_act == UserActType.NEGATE:
                        self.DST.clear()
                        return SystemAct(SystemActType.REQMORE, ['meeting_to_update'])
            else:
                return SystemAct(SystemActType.NOT_UNDERSTOOD, [])
        # stan anulowania spotkania
        elif dialogue_state == UserActType.CANCEL_MEETING:
            if not last_system_act:
                if 'date' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['date'])
                    self.DST.system_update(system_act)
                    return system_act
                elif 'time' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['time'])
                    self.DST.system_update(system_act)
                    return system_act
                else:
                    # implementacja wyszukiwania odpowiedniego spotkania w bazie
                    slots_to_delete = self.DB.find_meeting(slots['date'], slots['time'])
                    self.DST.update_slots(slots_to_delete)
                    #system_act = SystemAct(SystemActType.CONFIRM_DOMAIN, ['meeting_to_cancel'])
                    system_act = SystemAct(SystemActType.CONFIRM_DOMAIN, slots_to_delete)
                    self.DST.system_update(system_act)
                    return system_act
            elif last_system_act.getActType() == SystemActType.REQUEST:    
                if 'date' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['date'])
                    self.DST.system_update(system_act)
                    return system_act
                elif 'time' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['time'])
                    self.DST.system_update(system_act)
                    return system_act
                else:
                    # implementacja wyszukiwania odpowiedniego spotkania w bazie
                    slots_to_delete = self.DB.find_meeting(slots['date'], slots['time'])
                    self.DST.update_slots(slots_to_delete)
                    # system_act = SystemAct(SystemActType.CONFIRM_DOMAIN, ['meeting_to_cancel'])
                    system_act = SystemAct(SystemActType.CONFIRM_DOMAIN, slots_to_delete)
                    self.DST.system_update(system_act)
                    return system_act
            elif last_system_act.getActType() == SystemActType.CONFIRM_DOMAIN:
                if last_user_act == UserActType.CONFIRM:
                    system_act = SystemAct(SystemActType.AFFIRM, ['cancel_meeting'])
                    # implementacja usuwania spotkania z bazy
                    self.DB.delete_meeting(slots['date'], ['time'])
                    self.DST.clear()
                    return system_act
                elif last_user_act == UserActType.NEGATE:
                    self.DST.clear()
                    return SystemAct(SystemActType.REQMORE, ['cancel_meeting'])
            else:
                return SystemAct(SystemActType.NOT_UNDERSTOOD, [])
        # stan prośby o listę spotkań
        elif dialogue_state == UserActType.MEETING_LIST:
            if not last_system_act:
                if 'date' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['date'])
                    self.DST.system_update(system_act)
                    return system_act
                else:
                    # implementacja wyszukiwania spotkań w bazie
                    meetings_slots = self.DB.get_meetings([slots['date']])
                    system_act = SystemAct(SystemActType.MEETING_LIST, meetings_slots)
                    self.DST.system_update(system_act)
                    return system_act
            elif last_system_act.getActType() == SystemActType.REQUEST:
                if 'date' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['date'])
                    self.DST.system_update(system_act)
                    return system_act
                else:
                    # implementacja wyszukiwania spotkań w bazie
                    meetings_slots = self.DB.get_meetings([slots['date']])
                    system_act = SystemAct(SystemActType.MEETING_LIST, meetings_slots)
                    self.DST.system_update(system_act)
                    return system_act
            else:
                return SystemAct(SystemActType.NOT_UNDERSTOOD, [])
            # if last_user_act == UserActType.NEGATE:
            #     self.DST.clear()
            #     return SystemAct(SystemActType.REQMORE, ['meeting_list'])
            # else:
            #     if 'date' in slots:
            #         system_act = SystemAct(SystemActType.MEETING_LIST, slots)
            #         self.DST.clear()
            #         return system_act
            #     else:
            #         system_act = SystemAct(SystemActType.REQUEST, ['date'])
            #         self.DST.system_update(system_act)
            #         return system_act
        # stan prośby o czas wolny
        elif dialogue_state == UserActType.FREE_TIME:
            if last_user_act == UserActType.NEGATE:
                self.DST.clear()
                return SystemAct(SystemActType.REQMORE, ['free_time'])
            else:
                if 'date' in slots:
                    system_act = SystemAct(SystemActType.FREE_TIME, slots)
                    self.DST.clear()
                    return system_act
                else:
                    system_act = SystemAct(SystemActType.REQUEST, ['date'])
                    self.DST.system_update(system_act)
                    return system_act
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
