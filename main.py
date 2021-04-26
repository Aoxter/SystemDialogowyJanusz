from NaturalLanguageUnderstanding import NLU
from NaturalLanguageGeneration import NLG
from DialogueStateTracker import DST
from DialoguePolicy import DP

if __name__ == "__main__":

    nlu = NLU()
    dst = DST()
    dp = DP()
    nlg = NLG()

    while(1):
        user_input = input("Wpisz tekst: ")

        user_frame = nlu.parseUserInput(user_input)
        dst.addFrame(user_frame)
        system_act = dp.chooseTactic(dst.getFrames())
        text = nlg.toText(system_act)

        print(text)
        if system_act.isDialogFinished():
            break
