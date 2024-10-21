# Program pytający o oceny i wyliczający średnią

def dodaj_oceny():
    oceny = {}  # Słownik, gdzie kluczami będą nazwy przedmiotów, a wartościami listy ocen

    while True:
        przedmiot = input("Podaj nazwę przedmiotu: ").strip()  # Pobieramy nazwę przedmiotu od użytkownika
        ocena = float(input(f"Podaj ocenę dla {przedmiot}: "))  # Pobieramy ocenę dla podanego przedmiotu

        # Dodaj ocenę do odpowiedniego przedmiotu
        if przedmiot in oceny:
            oceny[przedmiot].append(ocena)  # Jeśli przedmiot już istnieje, dodajemy ocenę do jego listy
        else:
            oceny[przedmiot] = [ocena]  # Jeśli przedmiotu jeszcze nie ma, tworzymy nową listę z oceną

        # Pytamy, co chce zrobić użytkownik po wprowadzeniu oceny
        akcja = input("Chcesz dodać kolejną ocenę? (y/n) lub policzyć średnią (avg/wszystkie): ").strip().lower()

        if akcja == 'n':  # Jeśli użytkownik nie chce dodawać więcej ocen
            break
        elif akcja == 'avg':  # Liczenie średniej dla wybranego przedmiotu
            policz_srednia_z_przedmiotu(oceny)
        elif akcja == 'wszystkie':  # Liczenie średniej ze wszystkich przedmiotów
            policz_srednia_ogolna(oceny)

    # Po zakończeniu dodawania ocen, użytkownik może zdecydować, co dalej
    finalna_akcja = input("Policzyć średnią dla przedmiotu (avg) czy ze wszystkich (wszystkie)? ").strip().lower()
    if finalna_akcja == 'avg':
        policz_srednia_z_przedmiotu(oceny)
    elif finalna_akcja == 'wszystkie':
        policz_srednia_ogolna(oceny)

# Funkcja do liczenia średniej z wybranego przedmiotu
def policz_srednia_z_przedmiotu(oceny):
    przedmiot = input("Podaj nazwę przedmiotu, dla którego chcesz policzyć średnią: ").strip()
    if przedmiot in oceny:
        srednia = sum(oceny[przedmiot]) / len(oceny[przedmiot])
        print(f"Średnia z {przedmiot}: {srednia:.2f}")
    else:
        print(f"Nie ma ocen dla przedmiotu {przedmiot}")

# Funkcja do liczenia średniej z wszystkich przedmiotów
def policz_srednia_ogolna(oceny):
    suma_ocen = sum(sum(lista_ocen) for lista_ocen in oceny.values())
    liczba_ocen = sum(len(lista_ocen) for lista_ocen in oceny.values())
    srednia_ogolna = suma_ocen / liczba_ocen if liczba_ocen > 0 else 0
    print(f"Średnia ogólna: {srednia_ogolna:.2f}")

# Uruchomienie programu
dodaj_oceny()
