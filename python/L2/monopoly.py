import random

class Gracz:
    def __init__(self, name, pieniadze):
        self.name = name
        self.pieniadze = pieniadze
        self.pozycja = 0
        self.w_wiezieniu = False
        self.karta_wiezienie = False
        self.nieruchomosci = []
        self.ile_dworzec = 0
        self.ile_uzytek = 0
        self.ile_dom = 0
        self.ile_hotel = 0

    def przesun(self, ruchy, liczba_pol):
        self.pozycja = (self.pozycja + ruchy) % liczba_pol


class Pole:
    def __init__(self, name):
        self.name = name
        self.owner = None


class PoleNieruchomosc(Pole):
    def __init__(self, name, koszt, wynajem):
        super().__init__(name)
        self.koszt = koszt
        self.wynajem = wynajem


class Miasto(PoleNieruchomosc):
    def __init__(self, name, koszt, czynsz):
        super().__init__(name, koszt, czynsz[0])
        self.cena = koszt
        self.czynsz = czynsz
        self.ile_dom = 0
        self.ile_hotel = 0


class Uzytek(PoleNieruchomosc):
    pass


class Dworzec(PoleNieruchomosc):
    pass


class Kosc:
    def __init__(self):
        self.kosc_rzucona = False
        self.wynik_rzutu = 0
        self.ile_ruchu = 0

    def rzuc(self):
        self.kosc_rzucona = True
        self.wynik_rzutu = random.randint(1, 6)
        self.ile_ruchu = self.wynik_rzutu
        return self.wynik_rzutu


class Bankier:
    def __init__(self, suma_pieniadze):
        self.suma_pieniadze = suma_pieniadze

    def dodaj_pieniadze(self, gracz, kwota):
        gracz.pieniadze += kwota

    def zabierz_pieniadze(self, gracz, kwota):
        gracz.pieniadze -= kwota

    def ustaw_wlasciciela(self, pole, gracz):
        pole.owner = gracz


def main():
    random.seed()
    liczba_pol = 40

    # Tworzenie graczy
    grzegorz = Gracz("Grzegorz", 1500)
    janusz = Gracz("Janusz", 1500)

    # Tworzenie bankiera
    bankier = Bankier(10000)
    bankier.dodaj_pieniadze(grzegorz, 500)
    bankier.dodaj_pieniadze(janusz, 500)

    # Tworzenie nieruchomości
    aten = Miasto("Ateny", 200, [5, 15, 25, 35, 45, 55])
    madryt = Miasto("Madryt", 450, [15, 25, 35, 45, 55, 65])

    grzegorz.nieruchomosci.append(aten)
    janusz.nieruchomosci.append(madryt)

    # Tworzenie kostki
    kosc = Kosc()

    # Symulacja ruchu
    for _ in range(3):
        wynik_grzegorz = kosc.rzuc()
        print(f"Wynik rzutu Grzegorz: {wynik_grzegorz}")
        grzegorz.przesun(wynik_grzegorz, liczba_pol)

        wynik_janusz = kosc.rzuc()
        print(f"Wynik rzutu Janusz: {wynik_janusz}")
        janusz.przesun(wynik_janusz, liczba_pol)

    # Wyświetlanie wyników
    print(f"Pozycja Grzegorz: {grzegorz.pozycja}")
    print(f"Pieniądze Grzegorz: {grzegorz.pieniadze}")
    print("Miasta Grzegorz:", [miasto.name for miasto in grzegorz.nieruchomosci])

    print(f"Pozycja Janusz: {janusz.pozycja}")
    print(f"Pieniądze Janusz: {janusz.pieniadze}")
    print("Miasta Janusz:", [miasto.name for miasto in janusz.nieruchomosci])


if __name__ == "__main__":
    main()
