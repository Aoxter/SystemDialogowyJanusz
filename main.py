from SystemActType import SystemActType
from NaturalLanguageUnderstanding import NLU
from NaturalLanguageGeneration import NLG
from DialogueStateTracker import DST
from DialoguePolicy import DP

if __name__ == "__main__":

    nlu = NLU()
    dst = DST()
    dp = DP(dst)
    nlg = NLG(dst)

    while(1):
        user_input = input("Wpisz tekst: ")

        user_frame = nlu.parse_user_input(user_input)
        print('------ rozpoznany user frame ------')
        print(user_frame)
        dst.user_update(user_frame)
        state, last_user_act, last_system_act = dst.get_dialogue_state()
        slots = dst.get_dialogue_slots()
        system_act = dp.chooseTactic()

        print('------ stan ------')
        print(state, last_user_act, last_system_act)
        print('------ przechowywane sloty ------')
        print(slots)
        print('------ wybrana akcja systemu ------')
        print(system_act)
        system_response = nlg.generateResponse(system_act)
        print('------ wygenerowana odpowiedź systemu ------')
        print(system_response)
        print('-----------------------------------')
        print('-----------------------------------')
        
        if system_act.getActType() == SystemActType.BYE:
            break
