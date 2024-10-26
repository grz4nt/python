# Program pytający o oceny i wyliczający średnią

def menu():
    print("1. Dodaj ocenę")
    print("2. Oblicz średnią z przedmiotu")
    print("3. Oblicz średnią ze wszystkich przedmiotów")
    print("4. Zakończ program")
    return input("Wybierz opcję: ").strip()

def dodaj_oceny():
    oceny = {}  # Słownik, gdzie kluczami będą nazwy przedmiotów, a wartościami listy ocen

    while True:
        opcja = menu()

        if opcja == '1':  # Dodawanie ocen
            przedmiot = input("Podaj nazwę przedmiotu: ").strip()  # Pobieramy nazwę przedmiotu od użytkownika
            ocena = float(input(f"Podaj ocenę dla {przedmiot}: "))  # Pobieramy ocenę dla podanego przedmiotu

            # Dodaj ocenę do odpowiedniego przedmiotu
            if przedmiot in oceny:
                oceny[przedmiot].append(ocena)  # Jeśli przedmiot już istnieje, dodajemy ocenę do jego listy
            else:
                oceny[przedmiot] = [ocena]  # Jeśli przedmiotu jeszcze nie ma, tworzymy nową listę z oceną

            kontynuuj = input("Czy chcesz dodać kolejną ocenę? (y/n): ").strip().lower()
            if kontynuuj == 'n':
                continue  # Wracamy do menu

        elif opcja == '2':  # Liczenie średniej dla wybranego przedmiotu
            policz_srednia_z_przedmiotu(oceny)

        elif opcja == '3':  # Liczenie średniej ze wszystkich przedmiotów
            policz_srednia_ogolna(oceny)

        elif opcja == '4':  # Zakończenie programu
            print("Zakończono program.")
            break

        else:
            print("Niepoprawna opcja. Spróbuj ponownie.")

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
