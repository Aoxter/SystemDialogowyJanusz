from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)nazywam się (.*)",
        ["Cześć %2, jak się dzisiaj czujesz?",]
    ]
]

chatbot = Chat(pairs, reflections)

def hello():
    print("Przedstaw się\n")
    chatbot.converse()

if __name__ == "__main__":
    hello()