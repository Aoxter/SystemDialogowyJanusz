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

*user:* Dobrze, może być godzina 14:00.

*system:* Czy mam zapisać miejsce spotkania?

*user:* Tak, sala konferencyjna w biurze.

*system:* Czy mam zapisać naziwsko osoby, której dotyczy to spotkanie?

*user:* Tak, Jan Nowak - Prezes firmy ABC.

*system:* Czy mam dodać opis do spotkania?

*user:* Nie, nie trzeba.

*system:* Proszę potwierdzić utworzenie spotkania: <br>
          Data:           Poniedziałek 29.03.2021 14:00-15:00 <br>
          Miejsce:        Sala konferencyjna w biurze <br>
          Spotkanie z:    Jan Nowak - Prezes firmy ABC <br>

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

*system:* Obecna czas spotkania to Poniedziałek 29.03.2021 14:00-15:00, jaki ma być nowy czas spotkania?

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

*system:* Czy jesteś pewien, że chcesz odwołać poniższe spotkanie? <br>
            Data:           Poniedziałek 29.03.2021 16:00-17:15 <br>
            Miejsce:        Dom <br>
            Spotkanie z:    Kacper (Brat) <br>
            Opis:           Zaplanowanie imprezy urodzinowej dla mamy <br>

*user:* Tak.

*system:* Spotkanie zostało pomyślnie odwołane.


Zadanie 4: Podgląd spotkań względem daty
--------------------------

*system:* Witam w twoim prywatnym asystencie kalendarza spotkań.

*user:* Dzień dobry, chciałbym sprawdzić jutrzejsze spotkania.

*system:* Na jutro zaplanowano następujące spotkania: <br>
            Data:           Poniedziałek 29.03.2021 14:00-15:00 <br>
            Miejsce:        Sala konferencyjna w biurze <br>
            Spotkanie z:    Jan Nowak - Prezes firmy ABC <br>
            ------------------------------------------------------------------ <br>
            Data:           Poniedziałek 29.03.2021 16:00-17:15 <br>
            Miejsce:        Dom <br>
            Spotkanie z:    Kacper (Brat) <br>
            Opis:           Zaplanowanie imprezy urodzinowej dla mamy <br>

Zadanie 5: Podgląd spotkań względem umówionych osób
--------------------------

*system:* Witam w twoim prywatnym asystencie kalendarza spotkań.

*user:* Dzień dobry, chciałbym sprawdzić spotkania z Janem Nowakiem - Prezesem firmy ABC.

*system:* Z Janem Nowakiem - Prezesm firmy ABC umówione są następujące spotkania: <br>
            Data:           Poniedziałek 29.03.2021 14:00-15:00 <br>
            Miejsce:        Sala konferencyjna w biurze <br>
            Spotkanie z:    Jan Nowak - Prezes firmy ABC <br>
            ------------------------------------------------------------------ <br>
            Data:           Czwartek 1.04.2021 12:00-14:00 <br>
            Miejsce:        Firma ABC <br>
            Spotkanie z:    Jan Nowak - Prezes firmy ABC <br>
            Opis:           Omówienie warunków współpracy firm w ramach projektu XYZ. <br>


Zadanie 6: Podgląd spotkań względem miejsca
--------------------------

*system:* Witam w twoim prywatnym asystencie kalendarza spotkań.

*user:* Dzień dobry, chciałbym sprawdzić spotkania w moim domu.

*system:* W twoim domu umówione są następujące spotkania: <br>
            Data:           Poniedziałek 29.03.2021 16:00-17:15 <br>
            Miejsce:        Dom <br>
            Spotkanie z:    Kacper (Brat) <br>
            Opis:           Zaplanowanie imprezy urodzinowej dla mamy <br>
            ------------------------------------------------------------------ <br>
            Data:           Sobota 10.04.2021 11:00-18:00 <br>
            Miejsce:        Dom <br>
            Spotkanie z:    Rodzina <br>
            Opis:           Imprezy urodzinowa dla mamy <br>


Zadanie 7: Podgląd najbliższych spotkań
--------------------------

*system:* Witam w twoim prywatnym asystencie kalendarza spotkań.

*user:* Dzień dobry, chciałbym sprawdzić najbliższe spotkania.

*system:* Najbliższe spotkanie to: <br>
            Data:           Niedziela 28.03.2021 19:00 <br>
            Miejsce:        Brak <br>
            Spotkanie z:    Marek <br>
            Opis:           Spotkanie towarzyskie <br>
          Kolejne spotkanie to: <br>
            Data:           Poniedziałek 29.03.2021 14:00-15:00 <br>
            Miejsce:        Sala konferencyjna w biurze <br>
            Spotkanie z:    Jan Nowak - Prezes firmy ABC <br>
            
Zadanie 8: Podgląd wolnych terminow
--------------------------

*system:* Witam w twoim prywatnym asystencie kalendarza spotkań.

*user:* Dzień dobry, chciałbym sprawdzić najbliższe wolne terminy.

*system:* Najbliższe wolne terminy to: <br>
            Niedziela 28.03.2021: <br>
              - 12:00-19:00 <br>
            Poniedziałek 29.03.2021: <br>
              - 00:00-14:00 <br>
              - 15:00-16:00 <br>
              - 17:15-24:00 <br>