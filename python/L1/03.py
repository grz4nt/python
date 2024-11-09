def piramidka_z_tekstem():
    tekst = input("Podaj tekst: ").strip()
    dlugosc_tekstu = len(tekst)
    szerokosc_podstawy = dlugosc_tekstu + 4
    wysokosc = (szerokosc_podstawy // 2) + 1

    for i in range(wysokosc - 1):
        spacje_zewn = ' ' * (wysokosc - i - 1)
        spacje_wewn = ' ' * (2 * i + 1)
        if i == 0:
            print(f"{spacje_zewn}*")
        else:
            print(f"{spacje_zewn}*" + spacje_wewn + "*")
    
    print(f"* {tekst} *")
    print('*' * szerokosc_podstawy)

piramidka_z_tekstem()