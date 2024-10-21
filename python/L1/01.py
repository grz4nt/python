import math

def oblicz_kula(promien):
    objetosc = (4/3) * math.pi * promien**3
    pole = 4 * math.pi * promien**2
    return objetosc, pole

def oblicz_prostopadloscian(dlugosc, szerokosc, wysokosc):
    objetosc = dlugosc * szerokosc * wysokosc
    pole = 2 * (dlugosc * szerokosc + dlugosc * wysokosc + szerokosc * wysokosc)
    return objetosc, pole

def oblicz_stozek(promien, wysokosc):
    objetosc = (1/3) * math.pi * promien**2 * wysokosc
    tworzaca = math.sqrt(promien**2 + wysokosc**2)
    pole = math.pi * promien * (promien + tworzaca)
    return objetosc, pole

def main(bryla, wymiary):
    if bryla == "kula":
        return oblicz_kula(*wymiary)
    elif bryla == "prostopadloscian":
        return oblicz_prostopadloscian(*wymiary)
    elif bryla == "stozek":
        return oblicz_stozek(*wymiary)
    else:
        return "Nieprawidłowy wybór"

def menu():
    print("Wybierz bryłę:")
    print("1. Kula")
    print("2. Prostopadłościan")
    print("3. Stożek")
    
    wybor = input("Twój wybór (1-3): ")
    
    if wybor == '1':
        promien = float(input("Podaj promień kuli: "))
        wynik = main("kula", [promien])
    elif wybor == '2':
        print("Podaj wymiary prostopadłościanu:")
        dlugosc = float(input("długość: "))
        szerokosc = float(input("szerokość: "))
        wysokosc = float(input("wysokość: "))
        wynik = main("prostopadloscian", [dlugosc, szerokosc, wysokosc])
    elif wybor == '3':
        promien = float(input("Podaj promień podstawy stożka: "))
        wysokosc = float(input("wysokość: "))
        wynik = main("stozek", [promien, wysokosc])
    else:
        print("Nieprawidłowy wybór")
        return
    
    print(f"Objętość: {wynik[0]:.2f}")
    print(f"Pole powierzchni: {wynik[1]:.2f}")

menu()
