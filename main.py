import random


def utworz_pusta_plansze(rozmiar):
    """Tworzy pustą planszę w formie kwadratu o rozmiarze rozmiar"""
    tablica = [0] * rozmiar
    for i in range(rozmiar):
        tablica[i] = [" "] * rozmiar
    return tablica


def zapytanie(pytanie, domyslnie=True):
    """Zadaje pytanie i zwraca odpowiedź użytkownika"""
    odpowiedz = None
    while odpowiedz not in ("t", "n", ""):
        print(pytanie, end=" ")
        if domyslnie:
            print("(T/n)", end=" ")
        else:
            print("(t/N)", end=" ")
        odpowiedz = input().lower()
        if odpowiedz == "t":
            return True
        if odpowiedz == "n":
            return False
        if odpowiedz == "":
            return domyslnie


def kto_wygral():
    """zwraca X, O, albo False"""
    for x in range(0, ROZMIAR_PLANSZY):
        for y in range(0, ROZMIAR_PLANSZY):
            for kierunek in ("poziom", "pion", "skos prawy", "skos lewy"):
                iksy, kolka = sprawdz_linie((x, y), kierunek)
                if iksy == ile_do_wygranej:
                    return X
                if kolka == ile_do_wygranej:
                    return O
    return False


def wszystkie_zajete():
    """zwraca True, jeśli wszystkie pola są zajęte, a False, jeśli jest choć jedno wolne"""
    for i in plansza:
        if PUSTY in i:
            return False
    return True


def wyswietl_plansze():
    """Wyświetla planszę na ekranie"""
    print("-" * (ROZMIAR_PLANSZY * 4 + 1))
    for rzad in plansza:
        print("| ", end="")
        for element in rzad:
            print(element, end=" | ")
        print("")  # nowy wiersz
        print("-" * (ROZMIAR_PLANSZY * 4 + 1))


def wyswietl_mape(plansza):
    """Wyświetla mapę wartości pól na ekranie """
#    print(CLS)
    print("-" * (ROZMIAR_PLANSZY * 4 + 1))
    for rzad in plansza:
        print("| ", end="")
        for element in rzad:
            print(str(element), end=" | ")
        print("")  # nowy wiersz
        print("-" * (ROZMIAR_PLANSZY * 4 + 1))


def wprowadz_ruch(gracz):
    """Wprowadza ruch komputera lub człowieka do tablicy plansza[]"""
    if gracz == 'człowiek':
        return ruch_czlowieka()

    else:
        ruch_kompa()
        return True


def ruch_czlowieka():
    """Człowiek wybiera pole, albo qpisuje 'q' i wychodzi."""
    while True:
        x = None
        y = None
        while x not in range(0, ROZMIAR_PLANSZY) or y not in range(0, ROZMIAR_PLANSZY):
            x = input("x=")
            if x == 'q':
                return False
            y = input("y=")
            x = int(x) - 1
            y = int(y) - 1
        pole = (x, y)
        if plansza[y][x] == PUSTY:
            plansza[y][x] = czlowiek  # wstawiamy ruch do planszy
            return True
        else:
            print("To pole jest zajęte!")


def ruch_kompa():
    """Komputer wybiera pole, na którym postawi znak"""
    # definiujemy współczynniki dla linii zawierających znaki
    pusta_linia = 1

    jedenznak_p = 2
    dwaznaki_p = 8
    trzyznaki_p = 50
    czteryznaki_p = 1000

    jedenznak_k = -1
    dwaznaki_k = -1
    trzyznaki_k = 100
    czteryznaki_k = 900

    # tworzymy pustą mapę wartości pól
    mapa = [0] * ROZMIAR_PLANSZY
    for i in range(ROZMIAR_PLANSZY):
        mapa[i] = [0] * ROZMIAR_PLANSZY

    # wypełniamy wartościami
    for i in dozwolone_ruchy():
        wartosc = 0
        for kierunek in ("poziom", "pion", "skos prawy", "skos lewy"):
            for j in utworz_punkty_do_sprawdzenia(i, kierunek):
                iksy, kolka = sprawdz_linie(j, kierunek)
                if komputer == X:
                    if iksy == 0 and kolka == 0:
                        wartosc += pusta_linia
                    if iksy == 1 and kolka == 0:
                        wartosc += jedenznak_p
                    if iksy == 2 and kolka == 0:
                        wartosc += dwaznaki_p
                    if iksy == 3 and kolka == 0:
                        wartosc += trzyznaki_p
                    if iksy == 4 and kolka == 0:
                        wartosc += czteryznaki_p
                    # tutaj przeszkadzamy przeciwnikowi
                    if iksy == 0 and kolka == 1:
                        wartosc += jedenznak_k
                    if iksy == 0 and kolka == 2:
                        wartosc += dwaznaki_k
                    if iksy == 0 and kolka == 3:
                        wartosc += trzyznaki_k
                    if iksy == 0 and kolka == 4:
                        wartosc += czteryznaki_k
                if komputer == O:
                    if kolka == 0 and iksy == 0:
                        wartosc += pusta_linia
                    if kolka == 1 and iksy == 0:
                        wartosc += jedenznak_p
                    if kolka == 2 and iksy == 0:
                        wartosc += dwaznaki_p
                    if kolka == 3 and iksy == 0:
                        wartosc += trzyznaki_p
                    if kolka == 4 and iksy == 0:
                        wartosc += czteryznaki_p
                    # tutaj przeszkadzamy przeciwnikowi
                    if kolka == 0 and iksy == 1:
                        wartosc += jedenznak_k
                    if kolka == 0 and iksy == 2:
                        wartosc += dwaznaki_k
                    if kolka == 0 and iksy == 3:
                        wartosc += trzyznaki_k
                    if kolka == 0 and iksy == 4:
                        wartosc += czteryznaki_k

        mapa[i[1]][i[0]] = wartosc

    # szukamy wartości maksymalnej
    maksimum = 0
    for x in range(ROZMIAR_PLANSZY):
        for y in range(ROZMIAR_PLANSZY):
            if mapa[y][x] > maksimum:
                maksimum = mapa[y][x]

    pola_do_ruchu = ()
    for x in range(ROZMIAR_PLANSZY):
        for y in range(ROZMIAR_PLANSZY):
            if mapa[y][x] == maksimum:
                pola_do_ruchu += ((x, y),)

    ruch = random.choice(pola_do_ruchu)
    plansza[ruch[1]][ruch[0]] = komputer


def zmien_gracza(gracz):
    """zamienia strony gry czyli zawartość zmiennej 'gracz'"""
    if gracz == 'człowiek':
        return 'komputer'
    else:
        return 'człowiek'


def sprawdz_linie(pole, kierunek):
    """Sprawdza linię pole w podanym kierunku - 'poziom', 'pion', 'skos prawy' albo 'skos lewy'
       Zwraca <None, None>, jeśli linii nie da się utworzyć, albo ilość X i O jako dwie zmienne"""
    iksy = 0
    kolka = 0
    if kierunek == 'poziom':
        for x in range(pole[0], pole[0] + ile_do_wygranej):
            if x > ROZMIAR_PLANSZY - 1:
                return None, None  # pole poza planszą
            if plansza[pole[1]][x] == X:
                iksy += 1
            if plansza[pole[1]][x] == O:
                kolka += 1
    if kierunek == 'pion':
        for y in range(pole[1], pole[1] + ile_do_wygranej):
            if y > ROZMIAR_PLANSZY - 1:
                return None, None
            if plansza[y][pole[0]] == X:
                iksy += 1
            if plansza[y][pole[0]] == O:
                kolka += 1
    if kierunek == 'skos prawy':
        for xy in range(0, ile_do_wygranej):
            x = pole[0] + xy
            y = pole[1] + xy
            if x > ROZMIAR_PLANSZY - 1 or y > ROZMIAR_PLANSZY - 1:
                return None, None
            if plansza[y][x] == X:
                iksy += 1
            if plansza[y][x] == O:
                kolka += 1
    if kierunek == 'skos lewy':
        for xy in range(0, ile_do_wygranej):
            x = pole[0] - xy
            y = pole[1] + xy
            if x < 0 or y > ROZMIAR_PLANSZY - 1:
                return None, None
            if plansza[y][x] == X:
                iksy += 1
            if plansza[y][x] == O:
                kolka += 1
    return iksy, kolka


def utworz_punkty_do_sprawdzenia(xy, kierunek):
    x = xy[0]
    y = xy[1]
    punkty = ()
    if kierunek == 'poziom':
        for i in range(x - 4, x + 1):
            if i >= 0:
                punkty += ((i, y),)

    if kierunek == "pion":
        for i in range(y - 4, y + 1):
            if i >= 0:
                punkty += ((x, i),)

    if kierunek == "skos prawy":
        x = x - 4
        for i in range(y - 4, y + 1):
            if x >= 0 and i >= 0:
                punkty += ((x, i),)
            x += 1

    if kierunek == "skos lewy":
        x = x + 4
        for i in range(y - 4, y + 1):
            if i >= 0 and x < ROZMIAR_PLANSZY:
                punkty += ((x, i),)
            x -= 1

    return punkty


def dozwolone_ruchy():
    krotka = ()
    for x in range(0, ROZMIAR_PLANSZY):
        for y in range(0, ROZMIAR_PLANSZY):
            if plansza[y][x] == PUSTY:
                krotka += ((x, y),)
    return krotka


X = 'X'
O = 'O'
PUSTY = ' '
ROZMIAR_PLANSZY = int(input("Podaj rozmiar planszy: "))
ile_do_wygranej = int(input("Podaj ile znaków w lini lub w skosie prowadzi do wygranej: "))

plansza = utworz_pusta_plansze(ROZMIAR_PLANSZY)  # tworzymy tablicę - planszę do gry
czlowiek = None  # czym gra człowiek X czy O
komputer = None  # czym gra komputer

if zapytanie("Czy chcesz mieć pierwszy ruch?"):  # ustalamy, kto rusza się pierwszy
    czyj_ruch = 'człowiek'  #  kto gra X
    czlowiek = X
    komputer = O
else:
    czyj_ruch = 'komputer'
    czlowiek = O
    komputer = X

while not kto_wygral() and not wszystkie_zajete():
    wyswietl_plansze()
    if not wprowadz_ruch(czyj_ruch):
        break

    czyj_ruch = zmien_gracza(czyj_ruch)
wyswietl_plansze()
if kto_wygral():
    print("Wygrały: " + kto_wygral())