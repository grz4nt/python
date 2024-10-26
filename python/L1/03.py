def piramidka_z_tekstem():
    # Pobieramy tekst od użytkownika
    tekst = input("Podaj tekst: ").strip()
    
    # Długość tekstu i szerokość podstawy piramidki
    dlugosc_tekstu = len(tekst)
    szerokosc_podstawy = dlugosc_tekstu + 4  # Dodajemy 4 dla gwiazdek i spacji wokół tekstu

    # Liczba linii piramidki zależy od szerokości podstawy
    wysokosc = (szerokosc_podstawy // 2) + 1

    # Generowanie górnej części piramidki
    for i in range(wysokosc - 1):
        # Obliczamy liczbę spacji przed gwiazdkami i liczbę spacji między gwiazdkami
        spacje_zewn = ' ' * (wysokosc - i - 1)
        spacje_wewn = ' ' * (2 * i + 1)
        if i == 0:
            print(f"{spacje_zewn}*")
        else:
            print(f"{spacje_zewn}*" + spacje_wewn + "*")
    
    # Linia z tekstem
    print(f"* {tekst} *")

    # Generowanie dolnej linii (podstawa piramidki)
    print('*' * szerokosc_podstawy)

# Uruchomienie programu
piramidka_z_tekstem()
