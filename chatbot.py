from nltk.chat.util import Chat, reflections

pair1 = [
    [
        r"(.*)nazywam się (.*)",
        ["Cześć %2, jak się dzisiaj czujesz?",]
    ]
]

pair2 = [
    [
        r"(.*)czuję się (.*)",
        ["Cieszę się czujesz się %2?",]
    ]
]

pair3 = [

]

pair4 = [

]

chatbot = Chat(pair1+pair2+pair3+pair4, reflections)

def hello():
    print("Przedstaw się\n")
    chatbot.converse(quit='wyjdź')

if __name__ == "__main__":
    hello()