from SystemAct import SystemAct
from UserActType import UserActType
from SystemActType import SystemActType
from collections import defaultdict


class DP:
    def __init__(self, dst):
        self.DST = dst
        self.meeting_to_update = False

    def choose_tactic(self) -> SystemAct:
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
                    system_act = SystemAct(SystemActType.CONFIRM_DOMAIN, slots)
                    self.DST.system_update(system_act)
                    return system_act
            elif last_system_act.getActType() == SystemActType.CONFIRM_DOMAIN:
                if last_user_act == UserActType.CONFIRM:
                    system_act = SystemAct(SystemActType.AFFIRM, ['create_meeting'])
                    # implementacja wpisywanie spotkania do bazy
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
                    system_act = SystemAct(SystemActType.REQUEST, ['date', False])
                    self.DST.system_update(system_act)
                    return system_act
                elif 'time' not in slots:
                    system_act = SystemAct(SystemActType.REQUEST, ['time', False])
                    self.DST.system_update(system_act)
                    return system_act
                else:
                    # implementacja wyszukiwania odpowiedniego spotkania w bazie
                    return SystemAct(SystemActType.CONFIRM_DOMAIN, ['meeting_to_update'])
            elif last_system_act.getActType() == SystemActType.REQUEST:
                if not self.meeting_to_update:    
                    if 'date' not in slots:
                        system_act = SystemAct(SystemActType.REQUEST, ['date', False])
                        self.DST.system_update(system_act)
                        return system_act
                    elif 'time' not in slots:
                        system_act = SystemAct(SystemActType.REQUEST, ['time', False])
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
                            system_act = SystemAct(SystemActType.REQUEST, ['date', True])
                            self.DST.system_update(system_act)
                            return system_act
                        elif 'time' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['time', True])
                            self.DST.system_update(system_act)
                            return system_act
                        elif 'place' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['place', True])
                            self.DST.system_update(system_act)
                            return system_act
                        elif 'description' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['description', True])
                            self.DST.system_update(system_act)
                            return system_act
                        elif 'participants' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['participants', True])
                            self.DST.system_update(system_act)
                            return system_act
                        else:
                            system_act = SystemAct(SystemActType.CONFIRM_DOMAIN, slots)
                            self.DST.system_update(system_act)
                            return system_act
                    else:
                        if 'date' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['date', True])
                            self.DST.system_update(system_act)
                            return system_act
                        elif 'time' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['time', True])
                            self.DST.system_update(system_act)
                            return system_act
                        elif 'place' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['place', True])
                            self.DST.system_update(system_act)
                            return system_act
                        elif 'description' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['description', True])
                            self.DST.system_update(system_act)
                            return system_act
                        elif 'participants' not in slots:
                            system_act = SystemAct(SystemActType.REQUEST, ['participants', True])
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
                        system_act = SystemAct(SystemActType.REQUEST, ['date', True])
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
                    system_act = SystemAct(SystemActType.CONFIRM_DOMAIN, ['meeting_to_cancel'])
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
                    system_act = SystemAct(SystemActType.CONFIRM_DOMAIN, ['meeting_to_cancel'])
                    self.DST.system_update(system_act)
                    return system_act
            elif last_system_act.getActType() == SystemActType.CONFIRM_DOMAIN:
                if last_user_act == UserActType.CONFIRM:
                    system_act = SystemAct(SystemActType.AFFIRM, ['cancel_meeting'])
                    # implementacja usuwania spotkania z bazy
                    self.DST.clear()
                    return system_act
                elif last_user_act == UserActType.NEGATE:
                    self.DST.clear()
                    return SystemAct(SystemActType.REQMORE, ['cancel_meeting'])
            else:
                return SystemAct(SystemActType.NOT_UNDERSTOOD, [])
        # stan prośby o listę spotkań
        elif dialogue_state == UserActType.MEETING_LIST:
            if last_user_act == UserActType.NEGATE:
                self.DST.clear()
                return SystemAct(SystemActType.REQMORE, ['meeting_list'])
            else:
                if 'date' in slots:
                    system_act = SystemAct(SystemActType.MEETING_LIST, {'date': slots['date']})
                    return system_act
                else:
                    system_act = SystemAct(SystemActType.REQUEST, ['date'])
                    self.DST.system_update(system_act)
                    return system_act
        # stan prośby o czas wolny
        elif dialogue_state == UserActType.FREE_TIME:
            if last_user_act == UserActType.NEGATE:
                self.DST.clear()
                return SystemAct(SystemActType.REQMORE, ['free_time'])
            else:
                if 'date' in slots:
                    system_act = SystemAct(SystemActType.FREE_TIME, {'date': slots['date']})
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
