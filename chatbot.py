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
    [
        r"Co (.*)",
        [
            "Skąd to pytanie?",
            "Dlaczego pytasz?",
            "Nie wiem za bardzo co powiedzieć.",
            "A co ty o tym myślisz?",
        ],
    ],
    [
        r"Dlaczego (.*)",
        [
            "Prawdę mówiąc nigdy się nie zastanawiałem.",
            "A co ty o tym myślisz?",
            "Dlaczego akurat takie pytanie przyszło ci do głowy?",
        ],
    ],
    [
        r"Czemu (.*)",
        [
            "Odpowiedź na to pytanie nie jest prosta.",
            "Nigdy się nad tym nie zastanawiałem.",
        ],
    ],
    [
        r"(.*)\?",
        [
            "Myślę, że sam znasz odpowiedź na to pytanie.",
            "Może zastanów się nad tym chwilę.",
            "Co ty o tym sądzisz?",
        ],
    ],
]

pair4 = [

]

chatbot = Chat(pair1+pair2+pair3+pair4, reflections)

def hello():
    print("Przedstaw się\n")
    chatbot.converse(quit='wyjdź')

if __name__ == "__main__":
    hello()