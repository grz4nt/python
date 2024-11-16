# rozmiar piramidki, jeżeli większa niż długość tekstu to powiększ, jeśli mniejsza to tak jak z napisem

def piramidka():
    tekst = input("Podaj tekst: ").strip()
    dlugosc_tekstu = len(tekst)
    szerokosc_podstawy = dlugosc_tekstu + 6
    if szerokosc_podstawy % 2 == 0:
        wysokosc = szerokosc_podstawy // 2
    else:
        wysokosc = szerokosc_podstawy // 2 + 1

    for i in range(wysokosc - 1):
        even = False
        if dlugosc_tekstu % 2 == 0:
            even = True
        spacje_zewn = ' ' * (wysokosc - i)
        if even:
            spacje_wewn = ' ' * (2 * i - 2)
        else:
            spacje_wewn = ' ' * (2 * i - 1)
        if i == 0:
            print(f"{spacje_zewn}*")
        else:
            print(f"{spacje_zewn}*" + spacje_wewn + "*")
    
    spacje_po = szerokosc_podstawy - len(tekst) - 5
    print(f" * {tekst}{' ' * spacje_po}*")
    print('*' * szerokosc_podstawy)

piramidka()