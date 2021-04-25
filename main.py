from NaturalLanguageUnderstanding import NLU
from NaturalLAnguageGeneration import NLG
from DialogueStateTracker import DST
from DialoguePolicy import DP

if __name__ == "__main__":

    nlu = NLU()
    dst = DST()
    nlg = NLG()
    dp = DP()

    userFrame = nlu.parseUserInput("czesc")
    dst.addFrame(userFrame)
    systemAct = dp.chooseTactic(dst.getFrames())
    text = nlg.toText(systemAct)

    print(text)
