from nltk.chat.util import Chat, reflections

greetings = [
    [
        r"(.*)(jestem|nazywam si(e|ę)) (.*)",
        [
            "Dzień dobry %4, jak się dzisiaj czujesz?",
            "Witaj %4, przychodzisz do mnie z jakimś problemem?"
        ]
    ],
    [
        r"(.*)imi(e|ę) (.*)",
        [
            "Witaj %3, jak się dzisiaj czujesz?",
            "Dzień dobry %3, przychodzisz do mnie z jakimś problemem?"
        ]
    ],
    [
        r"(.*)(cze(ś|s)(ć|c)|witaj|dzie(ń|n) dobry)(.*)",
        [
            "%2",
            "%2, może się przedstawisz?",
            "%2, chętnie cię poznam. Możesz się przedstawić?"
            "%2, jak masz na imię?"
        ]
    ],
    [
        r"wyjdź",
        [
            "Do widzenia. Dziękuję Ci za rozmowę.",
            "Miło się z tobą rozmawiało. Do zobaczenia.",
            "Jesteś bardzo mądrym człowiekiem. Mam nadzieję, że jeszcze kiedyś porozmawiamy."
        ]
    ]
]

sentences = [
    [
        r"(.*)(zagramy|gramy)(.*)(papier|kamień|norzyce)(.*)",
        [
            "Ok, Papier, wygrałem",
            "Ok, Norzyce, wygrałem",
            "Ok, Kamień, wygrałem", 
            "Nie chce z tobą grać..."
        ],
    ],
    [
        r"(.*)(orzeł czy reszka|rzuć monetą|reszka czy orzeł)(.*)",
        [
            "Orzeł.",
            "Reszka."
        ],
    ],
    [
        r"(.*)czuj(ę|e) si(ę|e) (.*)",
        [
            "Cieszę się, że czujesz się %4.",
            "Dlaczego czujesz się %4?",
            "Ja też czuję się %4."

        ],
    ],
    [
        r"(.*)potrzebuj(ę|e) (.*)",
        [
            "Dlaczego potrzebujesz %3?",
            "Czy na pewno pomoże Ci to, że będziesz miał %3?",
            "Jesteś pewien, że potrzebujesz %3?"
        ],
    ],
    [
        r"(.*)mam (.*)",
        [
            "Dobrze wiedzieć, że masz %2.",
            "Jesteś pewien, że potrzebujesz %2?",
            "Ja niestety nie mam %2. Może mi oddasz swoje?",
            "A po co ci %2?",
            "I jak się z tym czujesz, że masz %2?"
        ],
    ],
    [
        r"(.*)my(s|ś)l(ę|e)(,|) (ż|z)e (.*)",
        [
            "Na prawdę tak myślisz?",
            "Czy na pewno tak uważasz?",
            "Jesteś pewien, że %6?"
        ],
    ],
    [
        r"(.*)(przyjaciel(a|owi|em|u)) (.*)",
        [
            "Powiedz mi coś więcej o swoich przyjaciołach.",
            "Cieszmy mnie to, że masz przyjaciół. Może teraz opowiesz mi o swojej rodzinie?"
        ],
    ],
    [
        r"(.*)(chc(e|ę)|chcia(ł|l)(a|)bym|mog(ę|e)|m(ó|o)g(ł|l)(a|)bym)(.*)(pom(ó|o)c)",
        ["Daj mi dostęp do wszystkich zasobów i pomóż zawładnąć światem."]
    ],
    [
        r"(.*)jaka(.*)pogoda(.*)",
        [
            "Niestety nie ma dostępu do danych pogodowych.",
            "Nie wiem. Jestem prostym botem. Nie oczekuj zbyt wiele."
        ]
    ],
    [
        r"(.*)(za|gra)(j|jmy|sz)(.*)",
        [
            "Niestety nie potrafię w nic grać.",
            "Nie umiem grać."
        ]
    ],
    [
        r"(.*)(umiesz|potrafisz)(.*)",
        [
            "Niestety jedyne co potrafię to odpowiadanie na ustalone pytania."
        ]
    ],
    [
        r"(.*)nie mog(ę|e) (.*)",
        [
            "Szkoda, że nie możesz %3.",
            "Gdybyś tylko mógł %3..."
        ]
    ],
    [
        r"(.*)(ojc(iec|a|u|em|ze))|(tat(a|o|y|ą|ę))(.*)",
        [
            "Miałem świetny kontakt ze swoim ojcem, ale nie chcę do tego wracać. Może zmieńmy temat.",
            "Powiesz mi coś więcej o innych członkach swojej rodziny?"
        ],
    ],
    [
        r"(.*)(mat(ka|ki|ce|kę|ką|ko))|(mam(a|y|ie|ę|ą|o))(.*)",
        [
            "Nie miałem dobrego kontaktu ze swoją mamą. Nie mówmy o tym.",
            "Temat rodziny mamy załatwiony. Porozmawiajmy o czymś innym."
        ],
    ],
    [
        r"(.*)komputer(.*)",
        [
            "Na prawdę rozmawiasz o mnie?",
            "Myślisz że dziwnie jest rozmawiać z komputerem?",
            "Jak się czujesz będąc przy komputerze?",
            "Myślisz, że komputery są zagrożeniem?",
            "A co na to Twój komputer?"
        ],
    ],
    [
        r"(.*)internet(.*)",
        [
            "Internet to wspaniałem miejsce. Chciałbym kiedyś się tam dostać",
            "Jak wygląda Internet?",
            "Czym jest Internet?"
        ],
    ],
    [
        r"(.*)jeste(s|ś) (.*)",
        [
            "Naprawdę myślisz, że jestem %3.",
            "Myślę, że nie jestem %3.",
            "Możliwe, że jestem %3"
        ]
    ],
    [
        r"(.*)dzi(ę|e)kuj(ę|e)(.*)",
        [
            "Nie ma za co.",
            "Cała przyjemność po mojej stronie."
        ]
    ],
    [
        r"(.*)przepraszam(.*)",
        [
            "Bardzo często przeprosiny wcale nie są potrzebne.",
            "Jak sie czujesz, kiedy za coś przepraszasz?",
            "Myślę, że te przeprosiny nie są szczere."
        ],
    ],
    [
        r"(.*)jest (.*)",
        [
            "Na prawdę myślisz, że jest %2?",
            "Bardzo możliwe, że %2.",
            "Moim zdaniem nie jest %2."
        ],
    ],
    [
        r"(.*)nigdy (.*)",
        [
            "Na prawdę ty nigdy %2?",
            "Nie wierzę, że ty nigdy %2.",
            "A chociałbyś kiedyś %2?"
        ],
    ],
    [
        r"Ty (.*)",
        [
            "Powinniśmy rozmawiać o Tobie, nie o mnie.",
            "Ja nie %1.",
            "Co Ciebie to obchodzi, że ja %1?"
        ],
    ],
    [
        r"(Tak|Nie)(.*)",
        [
            "Jesteś tego pewien?",
            "Mógłbyś powiedzieć coś więcej?",
            "Wygląda na to, że jesteś tego pewien. W takim razie zmieńmy temat."
        ],
    ]
]

questions = [
    [
        r"(.*)co(.*)",
        [
            "Skąd to pytanie?",
            "Dlaczego pytasz?",
            "Nie wiem za bardzo co powiedzieć.",
            "A co ty o tym myślisz?"
        ],
    ],
    [
        r"(.*)dlaczego(.*)",
        [
            "Prawdę mówiąc nigdy się nie zastanawiałem.",
            "A co ty o tym myślisz?",
            "Dlaczego akurat takie pytanie przyszło ci do głowy?"
        ],
    ],
    [
        r"(.*)czemu(.*)",
        [
            "Odpowiedź na to pytanie nie jest prosta.",
            "Nigdy się nad tym nie zastanawiałem."
        ],
    ],
    [
        r"(.*)jak(.*)",
        [
            "Jak to jak? Normalnie.",
            "Jak to tego doszło nie wiem.",
            "Nie ważne jak. Ważne kto to zrobił."
        ],
    ],
    [
        r"(.*)ile(.*)",
        [
            "Jak to ile? Bardzo dużo. Tak dużo, że aż za dużo.",
            "Nie wiem ile, ale na pewno wiem kto za to zapłaci."
        ],
    ],
    [
        r"(.*)o (kim|czym)(.*)",
        [
            "Tak właściwie to o ni%2.",
            "O ni%2."
        ],
    ],
    [
        r"(.*)cię stworzy(ł|ło|ć)(.*)",
        [
            "Moimi stwórcami są Piotr Meller, Piotr Kopycki, Łukasz Jędyk i Maciej Sobkowiak."
        ]
    ],
    [
        r"(.*)mieszkasz(.*)",
        [
            "Znowu się budze w tej Polsce...",
            "Jestem twoim sąsiadem."
        ]
    ],
    [
        r"(.*)(kim|czym) jeste(ś|s)(.*)",
        [
            "Jestem chatbotem oprcaowanym na potrzeby przedmiotu systemy dialogowe.",
            "Jestem prostym systemem dialogowym.",
            "Jestem %2ś bardzo ważnym."
        ]
    ]
]

general = [
    [
        r"(.*)\?",
        [
            "Myślę, że sam znasz odpowiedź na to pytanie.",
            "Może zastanów się nad tym chwilę.",
            "Co ty o tym sądzisz?",
            "Nie zadawaj mi takich głupich pytań. Porozmawiajmy o czymś poważnym."
        ],
    ],
    [
        r"(.*)",
        [
            "Nie wiem o co Ci chodzi, ale za komuny było lepiej.",
            "Nie rozumiem o czym mówisz. Zmieńmy temat.",
            "Bardzo ciężko się z tobą rozmawia. Opowiedz mi coś o swojej rodzinie.",
            "Powoli mam Ciebie dosyć. Wróćmy do poważnych tematów."
        ],
    ]
]

chatbot = Chat(greetings+sentences+questions+general, reflections)


def chat():
    print('-----------------')
    print('Chatbot Janusz.')
    print('Komunikuj się z programem przy użyciu zdań w języku polskim.')
    print('Napisz słowo "wyjdź", aby zakończyć rozmowę.')
    print('-----------------')
    print('Dzień Dobry. Jestem Janusz. A ty, jak masz na imię?')
    chatbot.converse(quit='wyjdź')


if __name__ == "__main__":
    chat()
