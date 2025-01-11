import random
import abc
import pickle
import os

class Pole(abc.ABC):
    def __init__(self, nazwa):
        self.nazwa = nazwa

    @abc.abstractmethod
    def akcja(self, gracz):
        """Abstrakcyjna metoda akcji dla danego pola"""
        pass

class PoleNieruchomosciowe(Pole):
    def __init__(self, nazwa, koszt, bazowy_czynsz):
        super().__init__(nazwa)
        self.wlasciciel = None
        self.koszt = koszt
        self.bazowy_czynsz = bazowy_czynsz
        self.poziom_ulepszenia = 0

    def akcja(self, gracz):
        if not self.wlasciciel:
            if gracz.pieniadze >= self.koszt:
                gracz.kup_nieruchomosc(self)
        elif self.wlasciciel != gracz:
            oplata = self.oblicz_czynsz()
            if gracz.pieniadze >= oplata:
                gracz.zaplac(oplata, self.wlasciciel)

    def oblicz_czynsz(self):
        return self.bazowy_czynsz * (1 + 0.5 * self.poziom_ulepszenia)

    def ulepsz(self):
        if self.poziom_ulepszenia < 4:
            self.poziom_ulepszenia += 1
            return True
        return False

class Miasto(PoleNieruchomosciowe):
    def __init__(self, nazwa, koszt, bazowy_czynsz):
        super().__init__(nazwa, koszt, bazowy_czynsz)

class Dworzec(PoleNieruchomosciowe):
    def __init__(self, nazwa, koszt):
        super().__init__(nazwa, koszt, bazowy_czynsz=50)

    def oblicz_czynsz(self):
        return self.bazowy_czynsz * (2 ** (self.wlasciciel.liczba_dworcy() - 1))

class UslugiUzytkowe(PoleNieruchomosciowe):
    def __init__(self, nazwa, koszt):
        super().__init__(nazwa, koszt, bazowy_czynsz=20)

    def oblicz_czynsz(self):
        return self.bazowy_czynsz * (10 ** (self.wlasciciel.liczba_uslug() - 1))

class Gracz:
    def __init__(self, nazwa, pieniadze=1500):
        self.nazwa = nazwa
        self.pieniadze = pieniadze
        self.pozycja = 0
        self.nieruchomosci = []

    def kup_nieruchomosc(self, nieruchomosc):
        if self.pieniadze >= nieruchomosc.koszt:
            self.pieniadze -= nieruchomosc.koszt
            self.nieruchomosci.append(nieruchomosc)
            nieruchomosc.wlasciciel = self

    def zaplac(self, kwota, odbiorca):
        if self.pieniadze >= kwota:
            self.pieniadze -= kwota
            odbiorca.pieniadze += kwota

    def liczba_dworcy(self):
        return sum(1 for n in self.nieruchomosci if isinstance(n, Dworzec))

    def liczba_uslug(self):
        return sum(1 for n in self.nieruchomosci if isinstance(n, UslugiUzytkowe))

class Plansza:
    def __init__(self):
        self.pola = [
            # Miasta
            Miasto("Warszawa", 250, 50),
            Miasto("Kraków", 200, 40),
            Miasto("Gdańsk", 180, 35),
            Miasto("Wrocław", 220, 45),
            Miasto("Poznań", 190, 38),
            Miasto("Łódź", 160, 32),
            Miasto("Katowice", 240, 48),
            Miasto("Lublin", 170, 34),
            Miasto("Szczecin", 210, 42),
            Miasto("Bydgoszcz", 180, 36),
            Miasto("Białystok", 150, 30),
            Miasto("Rzeszów", 190, 38),
            Miasto("Opole", 170, 34),
            Miasto("Zielona Góra", 160, 32),
            Miasto("Gorzów Wielkopolski", 180, 36),
            Miasto("Olsztyn", 190, 38),
            Miasto("Kielce", 170, 34),
            Miasto("Toruń", 160, 32),
            Miasto("Jelenia Góra", 180, 36),
            Miasto("Kalisz", 150, 30),
            Miasto("Elbląg", 140, 28),
            Miasto("Radom", 160, 32),

            # Dworce
            Dworzec("Dworzec Centralny", 300),
            Dworzec("Dworzec Zachodni", 250),
            Dworzec("Dworzec Wschodni", 250),
            Dworzec("Dworzec Południowy", 300),

            # Usługi użytkowe
            UslugiUzytkowe("Elektrownia", 250),
            UslugiUzytkowe("Wodociągi", 220),
            UslugiUzytkowe("Gazownia", 200)
        ]

class Gra:
    def __init__(self, gracze):
        self.plansza = Plansza()
        self.gracze = gracze
        self.tura = 0

    def wykonaj_ture(self):
        aktualny_gracz = self.gracze[self.tura % len(self.gracze)]
        rzut = random.randint(1, 6)
        aktualny_gracz.pozycja = (aktualny_gracz.pozycja + rzut) % len(self.plansza.pola)
        
        pole = self.plansza.pola[aktualny_gracz.pozycja]
        pole.akcja(aktualny_gracz)
        
        self.tura += 1

    def zapisz_stan(self, nazwa_pliku):
        with open(nazwa_pliku, 'wb') as plik:
            pickle.dump(self, plik)

    @classmethod
    def wczytaj_stan(cls, nazwa_pliku):
        with open(nazwa_pliku, 'rb') as plik:
            return pickle.load(plik)

def main():
    # Przykładowe użycie
    gracze = [Gracz("Gracz1"), Gracz("Gracz2")]
    gra = Gra(gracze)

    # Symulacja kilku tur
    for _ in range(10):
        gra.wykonaj_ture()

    # Zapis stanu gry
    gra.zapisz_stan("stan_gry.pkl")

    # Wczytanie stanu gry
    wczytana_gra = Gra.wczytaj_stan("stan_gry.pkl")

def demo_gry():
    # Stworzenie graczy
    gracz1 = Gracz("Grzegorz")
    gracz2 = Gracz("Janusz")
    gracze = [gracz1, gracz2]

    # Stworzenie planszy
    plansza = Plansza()

    print("Początkowy stan graczy:")
    for gracz in gracze:
        print(f"{gracz.nazwa}: pieniądze = {gracz.pieniadze}")

    # Symulacja 5 ruchów
    for i in range(5):
        print(f"\n--- Tura {i+1} ---")
        
        for gracz in gracze:
            # Rzut kostką
            rzut = random.randint(1, 6)
            print(f"{gracz.nazwa} rzuca kostką: {rzut}")
            
            # Zmiana pozycji
            gracz.pozycja = (gracz.pozycja + rzut) % len(plansza.pola)
            
            # Aktualne pole
            aktualnie_pole = plansza.pola[gracz.pozycja]
            print(f"{gracz.nazwa} trafia na pole: {aktualnie_pole.nazwa}")
            
            # Próba kupna pola
            if isinstance(aktualnie_pole, PoleNieruchomosciowe) and aktualnie_pole.wlasciciel is None:
                print(f"Próba kupna pola {aktualnie_pole.nazwa}")
                gracz.kup_nieruchomosc(aktualnie_pole)
                
                # Informacja o zakupie
                if aktualnie_pole.wlasciciel == gracz:
                    print(f"{gracz.nazwa} kupuje pole {aktualnie_pole.nazwa} za {aktualnie_pole.koszt}")
                else:
                    print(f"{gracz.nazwa} nie może kupić pola {aktualnie_pole.nazwa}")

        print("\nAktualny stan graczy:")
        for gracz in gracze:
            print(f"{gracz.nazwa}: pieniądze = {gracz.pieniadze}, pozycja = {gracz.pozycja}")
            print(f"Nieruchomości: {[n.nazwa for n in gracz.nieruchomosci]}")

if __name__ == "__main__":
    main()
    demo_gry()