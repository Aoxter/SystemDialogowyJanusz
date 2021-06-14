from SystemActType import SystemActType
from NaturalLanguageUnderstanding import NLU
from NaturalLanguageGeneration import NLG
from DialogueStateTracker import DST
from DialoguePolicy import DP
from DBManager import calender_db

if __name__ == "__main__":
    db = calender_db()
    nlu = NLU()
    dst = DST()
    dp = DP(dst, db)
    nlg = NLG(dst)

    while(1):
        user_input = input("\nWpisz tekst: ")

        user_frame = nlu.parse_user_input(user_input)
        print('\n------ rozpoznany user frame ------')
        print(user_frame)

        dst.user_update(user_frame)
        state, last_user_act, last_system_act = dst.get_dialogue_state()
        slots = dst.get_dialogue_slots()
        system_act = dp.chooseTactic()

        print('\n------ stan ------')
        print(state, last_user_act, last_system_act)
        print('\n------ przechowywane sloty ------')
        print(slots)
        print('\n------ wybrana akcja systemu ------')
        print(system_act)
        system_response = nlg.generateResponse(system_act)
        print('\n------ wygenerowana odpowiedź systemu ------')
        print(system_response)
        
        if system_act.getActType() == SystemActType.BYE:
            break
