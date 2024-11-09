def menu():
    print("1. Dodaj ocenę")
    print("2. Oblicz średnią z przedmiotu")
    print("3. Oblicz średnią ze wszystkich przedmiotów")
    print("4. Zakończ program")
    return input("Wybierz opcję: ").strip()

def wprowadz_ocene(oceny, przedmiot):
    ocena = float(input(f"Podaj ocenę dla {przedmiot}: "))

    if przedmiot in oceny:
        oceny[przedmiot].append(ocena)
    else:
        oceny[przedmiot] = [ocena]

def dodaj_oceny():
    oceny = {}

    while True:
        opcja = menu()

        if opcja == '1':
            przedmiot = input("Podaj nazwę przedmiotu: ").strip() 
            while True:
                wprowadz_ocene(oceny, przedmiot)
                kontynuuj = input("Czy chcesz dodać kolejną ocenę dla tego samego przedmiotu? [t/n]: ").strip().lower()
                if kontynuuj == 'n':
                    break

        elif opcja == '2':
            policz_srednia_z_przedmiotu(oceny)

        elif opcja == '3':
            policz_srednia_ogolna(oceny)

        elif opcja == '4':
            print("Zakończono program.")
            break

        else:
            print("Niepoprawna opcja. Spróbuj ponownie.")

def policz_srednia_z_przedmiotu(oceny):
    przedmiot = input("Podaj nazwę przedmiotu, dla którego chcesz policzyć średnią: ").strip()
    if przedmiot in oceny:
        srednia = sum(oceny[przedmiot]) / len(oceny[przedmiot])
        print(f"Średnia z przedmiotu {przedmiot}: {srednia:.2f}")
    else:
        print(f"Nie ma ocen dla przedmiotu {przedmiot}")

def policz_srednia_ogolna(oceny):
    suma_ocen = sum(sum(lista_ocen) for lista_ocen in oceny.values())
    liczba_ocen = sum(len(lista_ocen) for lista_ocen in oceny.values())
    srednia_ogolna = suma_ocen / liczba_ocen if liczba_ocen > 0 else 0
    print(f"Średnia ogólna: {srednia_ogolna:.2f}")

dodaj_oceny()