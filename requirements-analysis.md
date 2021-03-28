Asystent kalendarza spotkań
==============

Zadanie 1: Umawianie spotkania
--------------------------------

*system:* Witam w twoim prywatnym asystencie kalendarza spotkań.

*user:* Dzień dobry, chciałbym umówić nowe spotkanie.

*system:* Proszę podać dzień na jaki mam umówić spotkanie.

*user:* Najbliższy poniedziałek.

*system:* Proszę podać godzinę i długość spotkania.

*user:* 15:30, 1 godzina 

*system:* Niestety, godzina ta jest już zajęta przez inne spotkanie, proponuję godzinę 14:00.

*user:* Zgadzam się.

*system:* Czy mam zapisać miejsce spotkania?

*user:* Tak, sala konferencyjna w biurze.

*system:* Czy mam zapisać naziwsko osoby, której dotyczy to spotkanie?

*user:* Tak, Jan Nowak - Prezes firmy ABC.

*system:* Czy mam dodać opis do spotkania?

*user:* Nie, nie trzeba.

*system:* Proszę potwierdzić utworzenie spotkania:
            Data:           Poniedziałek 29.03.2021 14:00-15:00
            Miejsce:        Sala konferencyjna w biurze
            Spotkanie z:    Jan Nowak - Prezes firmy ABC 

*user:* Zatwierdzam.

*system:* Spotkanie zostało pomyślnie dodane do kalendarza.


Zadanie 2: Edycja spotkania
--------------------------

*system:* Witam w twoim prywatnym asystencie kalendarza spotkań.

*user:* Dzień dobry, chciałbym edytować spotkanie.

*system:* Proszę podać datę i godzinę spotkania do edycji.

*user:* 29.03.2021 14:00

*system:* Czego ma dytyczyć edycja? Czasu, miejsca, osoby czy opisu?

*user:* Osoby.

*system:* Obecna osoba to Jan Nowak - Prezes firmy ABC, kogo ma dotyczyć to spotkanie?

*user:* Adam Kowalski - Wiceprezes firmy ABC.

*system:* Czy to wszystkie zmiany?

*user:* Nie, chciałbym jeszcze zmienić czas spotkania.

*system:* Obecna czas spotkania to Poniedziałek 29.03.2021 14:00-15:00, jaki ma być nowy czas       spotkania?

*user:* Niech zostanie bez zmian.

*system:* Czas nie został zmieniony, czy to wszystkie edycje?

*user:* Tak.

*system:* Spotkanie zostało pomyślnie zmienione.


Zadanie 3: Odwołanie spotkania
--------------------------

*system:* Witam w twoim prywatnym asystencie kalendarza spotkań.

*user:* Dzień dobry, chciałbym odwołać spotkanie.

*system:* Proszę podać datę i godzinę spotkania do odwołania.

*user:* 29.03.2021 16:00

*system:* Czy mam odwołąć poniższe spotkanie?
            Data:           Poniedziałek 29.03.2021 16:00-17:15
            Miejsce:        Dom
            Spotkanie z:    Kacper (Brat)
            Opis:           Zaplanowanie imprezy urodzinowej dla mamy

*user:* Tak.

*system:* Spotkanie zostało pomyślnie odwołane.


Zadanie 4: Podgląd spotkań względem daty
--------------------------

*system:* Witam w twoim prywatnym asystencie kalendarza spotkań.

*user:* Dzień dobry, chciałbym sprawdzić jutrzejsze spotkania.

*system:* Na jutro zaplanowano następujące spotkania:
            Data:           Poniedziałek 29.03.2021 14:00-15:00
            Miejsce:        Sala konferencyjna w biurze
            Spotkanie z:    Jan Nowak - Prezes firmy ABC 
            ------------------------------------------------------------------
            Data:           Poniedziałek 29.03.2021 16:00-17:15
            Miejsce:        Dom
            Spotkanie z:    Kacper (Brat)
            Opis:           Zaplanowanie imprezy urodzinowej dla mamy


Zadanie 5: Podgląd spotkań względem umówionych osób
--------------------------

*system:* Witam w twoim prywatnym asystencie kalendarza spotkań.

*user:* Dzień dobry, chciałbym sprawdzić spotkania z Janem Nowakiem - Prezesem firmy ABC.

*system:* Z Janem Nowakiem - Prezesm firmy ABC umówione są następujące spotkania:
            Data:           Poniedziałek 29.03.2021 14:00-15:00
            Miejsce:        Sala konferencyjna w biurze
            Spotkanie z:    Jan Nowak - Prezes firmy ABC 
            ------------------------------------------------------------------
            Data:           Czwartek 1.04.2021 12:00-14:00
            Miejsce:        Firma ABC
            Spotkanie z:    Jan Nowak - Prezes firmy ABC 
            Opis:           Omówienie warunków współpracy firm w ramach projektu XYZ.


Zadanie 6: Podgląd spotkań względem kategorii
--------------------------



Zadanie 7: Podgląd spotkań względem miejsca
--------------------------

*system:* Witam w twoim prywatnym asystencie kalendarza spotkań.

*user:* Dzień dobry, chciałbym sprawdzić spotkania w moim domu.

*system:* W domu umówione są następujące spotkania:
            Data:           Poniedziałek 29.03.2021 16:00-17:15
            Miejsce:        Dom
            Spotkanie z:    Kacper (Brat)
            Opis:           Zaplanowanie imprezy urodzinowej dla mamy
            ------------------------------------------------------------------
            Data:           Sobota 10.04.2021 11:00-18:00
            Miejsce:        Dom
            Spotkanie z:    Rodzina
            Opis:           Imprezy urodzinows dla mamy


Zadanie 8: Podgląd najbliższych spotkań
--------------------------

*system:* Witam w twoim prywatnym asystencie kalendarza spotkań.

*user:* Dzień dobry, chciałbym sprawdzić najbliższe spotkania.

*system:* Najbliższe spotkanie to:
            Data:           Niedziela 28.03.2021 19:00
            Miejsce:        Brak
            Spotkanie z:    Marek
            Opis:           Spotkanie towarzyskie
          Kolejne spotkanie to:
            Data:           Poniedziałek 29.03.2021 14:00-15:00
            Miejsce:        Sala konferencyjna w biurze
            Spotkanie z:    Jan Nowak - Prezes firmy ABC 
            
Zadanie 9: Podgląd wolnych terminow
--------------------------

*system:* Witam w twoim prywatnym asystencie kalendarza spotkań.

*user:* Dzień dobry, chciałbym sprawdzić najbliższe wolne terminy.

*system:* Najbliższe wolne terminy to:
            Niedziela 28.03.2021:
                12:00-19:00
            Poniedziałek 29.03.2021:
                00:00-14:00
                15:00-16:00
                17:15-24:00