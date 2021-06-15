from SystemAct import SystemAct
from SystemActType import SystemActType
from UserActType import UserActType

class NLG:
    """
    Moduł, który tworzy reprezentację tekstową aktu systemowego wybranego przez taktykę dialogu.
    Wejście: Akt systemu (rama)
    Wyjście: Tekst
    """

    def __init__(self, dst):
        self.DST = dst

    def generateResponse(self, systemAct: SystemAct) -> str:
        dialogue_state, _, last_system_act = self.DST.get_dialogue_state()
        slots = self.DST.get_dialogue_slots()
        if dialogue_state == UserActType.CREATE_MEETING:
            if systemAct.getActType() == SystemActType.REQUEST:
                if "date" in systemAct.getActParams():
                    return "W jakim dniu ma się odbyć to spotkanie?"
                if "time" in systemAct.getActParams():
                    return "W jakim czasie ma się odbyć to spotkanie?"
                if "place" in systemAct.getActParams():
                    return "Gdzie ma się odbyć to spotkanie?"
                if "description" in systemAct.getActParams():
                    return "Czy mam dodać jakiś opis do tego spotkania?"
                if "participants" in systemAct.getActParams():
                    return "Kto ma wziąć udział w spotkaniu?"
            if systemAct.getActType() == SystemActType.CONFIRM_DOMAIN:
                date = slots['date']
                time = slots['time']
                place = slots['place']
                part_list = slots['participants']
                part = ""
                if part_list is None:
                    part = None
                else:
                    for p in part_list:
                        part += p
                        part += ", "
                    part = part[:-2]
                desc = slots['description']
                return f'Czy mam dodać te spotkanie do kalendarza?\n' \
                       f'Dzień: {date}\nCzas: {time}\nMiejsce: {place}\nUczestnicy: {part}\nOpis: {desc}'

        # TODO: nie sprawdzone - trudno wejść do tego stanu
        elif dialogue_state == UserActType.UPDATE_MEETING:
            if systemAct.getActType() == SystemActType.REQUEST:
                if "date" in systemAct.getActParams():
                    return "W jakim dniu miało się odbyć to spotkanie?"
                if "time" in systemAct.getActParams():
                    return "W jakim czasie miało się odbyć to spotkanie?"
            # TODO dopracować po dodaniu DB
            if systemAct.getActType() == SystemActType.CONFIRM_DOMAIN:
                date = slots['date']
                time = slots['time']
                place = slots['place']
                part_list = slots['participants']
                part = ""
                if part_list is None:
                    part = None
                else:
                    for p in part_list:
                        part += p
                        part += ", "
                    part = part[:-2]
                desc = slots['description']
                return f'Spotkanie:\n' \
                       f'Dzień: {date}\nCzas: {time}\nMiejsce: {place}\nUczestnicy: {part}\nOpis: {desc}'

        elif dialogue_state == UserActType.CANCEL_MEETING:
            if systemAct.getActType() == SystemActType.REQUEST:
                if "date" in systemAct.getActParams():
                    return "W jakim dniu miało się odbyć to spotkanie?"
                if "time" in systemAct.getActParams():
                    return "W jakim czasie miało się odbyć to spotkanie?"
            if systemAct.getActType() == SystemActType.CONFIRM_DOMAIN:
                date = slots['date']
                time = slots['time']
                place = slots['place']
                part_list = slots['participants']
                part = ""
                if part_list is None:
                    part = None
                else:
                    for p in part_list:
                        part += p
                        part += ", "
                    part = part[:-2]
                desc = slots['description']
                return f'Odwołać te spotkanie?:\n' \
                       f'Dzień: {date}\nCzas: {time}\nMiejsce: {place}\nUczestnicy: {part}\nOpis: {desc}'

        elif dialogue_state == UserActType.MEETING_LIST:
            if systemAct.getActType() == SystemActType.REQUEST:
                if "date" in systemAct.getActParams():
                    return "Z jakiego okresu chcesz przejrzeć spotkania?"
            if systemAct.getActType() == SystemActType.MEETING_LIST:
                response = ""
                for s in last_system_act.getActParams():
                    date = s['date']
                    time = s['time']
                    place = s['place']
                    part_list = s['participants']
                    part = ""
                    if part_list is None:
                        part = None
                    else:
                        for p in part_list:
                            part += p
                            part += ", "
                        part = part[:-2]
                    desc = s['description']
                    response += f'\nSpotkanie:\nDzień: {date}\nCzas: {time}\nMiejsce: {place}\nUczestnicy: {part}\nOpis: {desc}\n'
                    response += "--------------------"
                self.DST.clear()
                return response

        elif dialogue_state == UserActType.FREE_TIME:
            if systemAct.getActType() == SystemActType.REQUEST:
                if "date" in systemAct.getActParams():
                    return "W jakim okresie chcesz znaleźć wolny czas?"
            # TODO: dopracować po dodaniu DB
            if systemAct.getActType() == SystemActType.FREE_TIME:
                response = ""
                for s in slots:
                    date = s['date']
                    time = s['time']
                    response += f'Spotkanie:\nDzień: {date}\nCzas: {time}\n'
                return response

        elif systemAct.getActType() == SystemActType.AFFIRM:
            if "create_meeting" in systemAct.getActParams():
                return "Spotkanie zostało dodane"
            if "update_meeting" in systemAct.getActParams():
                return "Spotkanie zostało zaktualizowane"
            if "cancel_meeting" in systemAct.getActParams():
                return "Spotkanie zostało odwołane"

        elif systemAct.getActType() == SystemActType.REQMORE:
            if "create_meeting" in systemAct.getActParams():
                return "Spotkanie zostało odrzucone. Mogę pomóc w czymś jeszcze?"
            if "update_meeting" in systemAct.getActParams():
                return "Aktualizacja spotkania została anulowana. Mogę pomóc w czymś jeszcze?"
            if "cancel_meeting" in systemAct.getActParams():
                return "Odwoływanie spotkania zostało anulowane. Mogę pomóc w czymś jeszcze?"
            if "meeting_list" in systemAct.getActParams() or "free_time" in systemAct.getActParams():
                return "Mogę pomóc w czymś jeszcze?"

        else:
            if systemAct.getActType() == SystemActType.WELCOME_MSG:
                return "Cześć"
            if systemAct.getActType() == SystemActType.REQMORE:
                return "Czy mogę Ci w czymś jeszcze pomóc?"
            if systemAct.getActType() == SystemActType.BYE:
                return "Do widzenia."
            if systemAct.getActType() == SystemActType.NOT_UNDERSTOOD:
                return "Nie rozumiem o czym mówisz."

        # TODO: Not implemented in DP
        # if systemAct.getActType() == SystemActType.INFORM:
        #     if "name" in systemAct.getActParams():
        #         return "Nazywam się Janusz"
        raise Exception("SystemAct:{} not recognized".format(systemAct))
