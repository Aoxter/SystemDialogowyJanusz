from NaturalLanguageUnderstanding import NLU
from NaturalLanguageGeneration import NLG
from DialogueStateTracker import DST
from DialoguePolicy import DP

if __name__ == "__main__":

    nlu = NLU()
    dst = DST()
    dp = DP(dst)
    nlg = NLG()

    while(1):
        user_input = input("Wpisz tekst: ")

        user_frame = nlu.parse_user_input(user_input)
        print('------ rozpoznany user frame ------')
        print(user_frame)
        dst.user_update(user_frame)
        state, last_user_act, last_system_act = dst.get_dialogue_state()
        slots = dst.get_dialogue_slots()
        system_act = dp.chooseTactic()
        dst.system_update(system_act)
        print('------ stan ------')
        print(state, last_user_act, last_system_act)
        print('------ przechowywane sloty ------')
        print(slots)
        print('------ wybrana akcja systemu ------')
        print(system_act)
        print('-----------------------------------')
        print('-----------------------------------')
        #text = nlg.toText(system_act)

        #print(text)
        #if system_act.isDialogFinished():
        #    break
