import random
import csv
import os

def generuj_pesel():
    """
    Generuje losowy 11-cyfrowy PESEL z uwzględnieniem liczby dni w miesiącu:
    - [AA]: dowolne 2 cyfry
    - [BB]: miesiąc (01-12)
    - [CC]: dzień zgodny z liczbą dni w miesiącu
    - [DDDDD]: 5 dowolnych cyfr
    """
    # Pierwsza para cyfr (dowolne)
    para_aa = str(random.randint(0, 99)).zfill(2)
    
    # Miesięcy zawsze od 01 do 12
    miesiac = random.randint(1, 12)
    para_bb = str(miesiac).zfill(2)
    
    # Ustalenie max liczby dni w miesiącu
    if miesiac == 2:
        # Luty - maksymalnie 28 dni
        max_dni = 28
    elif miesiac < 8:
        # Miesiące do lipca: nieparzyste mają 31, parzyste 30 dni
        max_dni = 31 if miesiac % 2 == 1 else 30
    else:
        # Od sierpnia: nieparzyste mają 30, parzyste 31 dni
        max_dni = 30 if miesiac % 2 == 1 else 31
    
    # Dzień od 01 do max_dni
    para_cc = str(random.randint(1, max_dni)).zfill(2)
    
    # 5 losowych cyfr na końcu
    para_ddddd = ''.join(str(random.randint(0, 9)) for _ in range(5))
    
    return para_aa + para_bb + para_cc + para_ddddd

def wczytaj_dane_z_pliku(nazwa_pliku):
    """Wczytuje dane z pliku CSV."""
    with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
        return [linia.strip() for linia in plik]

def wczytaj_istniejace_dane(sciezka_pliku):
    """
    Wczytuje istniejące dane z pliku CSV, aby uniknąć duplikatów.
    Zwraca zbiór krotek reprezentujących już istniejące rekordy.
    """
    istniejace_dane = set()
    
    # Sprawdzamy czy plik istnieje
    if not os.path.exists(sciezka_pliku):
        return istniejace_dane
    
    with open(sciezka_pliku, 'r', encoding='utf-8') as plik:
        csvreader = csv.reader(plik, delimiter=';')
        # Pomijamy nagłówek
        next(csvreader, None)
        
        for wiersz in csvreader:
            # Dodajemy rekord jako krotkę (bez nagłówka)
            if len(wiersz) > 0:
                istniejace_dane.add(tuple(wiersz))
    
    return istniejace_dane

def generuj_dane_osobowe(liczba_wierszy, istniejace_dane):
    """Generuje losowe dane osobowe."""
    # Wczytaj dane z plików
    imiona = wczytaj_dane_z_pliku('imiona.csv')
    nazwiska = wczytaj_dane_z_pliku('nazwiska.csv')
    ulice = wczytaj_dane_z_pliku('ulice.csv')
    miasta = wczytaj_dane_z_pliku('miasta.csv')
    kraje = wczytaj_dane_z_pliku('kraje.csv')

    # Zbiór do przechowywania nowych unikalnych wierszy
    wygenerowane_dane = set()

    while len(wygenerowane_dane) < liczba_wierszy:
        # Losuj dane
        dane = (
            random.choice(imiona),
            random.choice(nazwiska),
            generuj_pesel(),
            random.choice(ulice),
            str(random.randint(1, 50)),
            random.choice(miasta),
            random.choice(kraje)
        )
        
        # Sprawdzamy czy dane nie istnieją już w istniejących danych
        if dane not in istniejace_dane:
            wygenerowane_dane.add(dane)

    return list(wygenerowane_dane)

def wyswietl_rekord(sciezka_pliku, numer_linii):
    """
    Wyświetla rekord z pliku CSV o podanym numerze linii.
    
    :param sciezka_pliku: Ścieżka do pliku CSV
    :param numer_linii: Numer linii do wyświetlenia (pomijając nagłówek)
    """
    try:
        with open(sciezka_pliku, 'r', encoding='utf-8') as plik:
            # Pomijamy nagłówek
            csvreader = csv.reader(plik, delimiter=';')
            next(csvreader)
            
            # Przechodzenie do konkretnej linii
            for i, wiersz in enumerate(csvreader, start=1):
                if i == numer_linii:
                    # Wyświetlanie rekordu w czytelnym formacie
                    print("\nSzczegóły rekordu:")
                    print(f"Imię: {wiersz[0]}")
                    print(f"Nazwisko: {wiersz[1]}")
                    print(f"PESEL: {wiersz[2]}")
                    print(f"Ulica: {wiersz[3]}")
                    print(f"Numer domu: {wiersz[4]}")
                    print(f"Miasto: {wiersz[5]}")
                    print(f"Kraj: {wiersz[6]}")
                    return
            
            print(f"Nie znaleziono rekordu o numerze linii {numer_linii}")
    
    except FileNotFoundError:
        print(f"Nie można otworzyć pliku {sciezka_pliku}")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

def main():
    sciezka_pliku = 'dane.csv'
    
    # Wczytaj istniejące dane, aby uniknąć duplikatów
    istniejace_dane = wczytaj_istniejace_dane(sciezka_pliku)

    while True:
        try:
            liczba_wierszy = int(input("Podaj liczbę wierszy do wygenerowania: "))
            if liczba_wierszy > 0:
                break
            else:
                print("Liczba wierszy musi być dodatnia!")
        except ValueError:
            print("Proszę podać poprawną liczbę!")

    # Generuj dane
    nowe_dane = generuj_dane_osobowe(liczba_wierszy, istniejace_dane)

    # Zapis do pliku - tryb dołączania ('a'), aby nie nadpisywać
    tryb_zapisu = 'a' if os.path.exists(sciezka_pliku) else 'w'
    with open(sciezka_pliku, tryb_zapisu, encoding='utf-8', newline='') as plik:
        writer = csv.writer(plik, delimiter=';')
        
        # Dodaj nagłówek tylko jeśli plik jest pusty
        if tryb_zapisu == 'w':
            writer.writerow(['imie', 'nazwisko', 'pesel', 'ulica', 'nr_domu', 'miasto', 'kraj'])
        
        # Zapis nowych danych
        writer.writerows(nowe_dane)

    print(f"Wygenerowano {len(nowe_dane)} unikalnych wierszy w pliku {sciezka_pliku}")

    # Opcja wyświetlenia rekordu
    while True:
        wybor = input("\nCzy chcesz wyświetlić rekord? (t/n): ").lower()
        if wybor != 't':
            break
        
        try:
            numer_linii = int(input("Podaj numer linii rekordu do wyświetlenia: "))
            wyswietl_rekord(sciezka_pliku, numer_linii)
        except ValueError:
            print("Proszę podać poprawny numer linii!")

if __name__ == "__main__":
    main()