import funkcje

def main():
    numbers = []
    print("Podaj 15 liczb całkowitych:")
    for i in range(15):
        num = int(input(f"Liczba {i + 1}: "))
        numbers.append(num)
    
    min_value, min_pos, max_value, max_pos = funkcje.find_min_max(numbers)
    
    avg_value = funkcje.calculate_average(numbers)

    search_value = int(input("Podaj liczbę do wyszukania: "))
    position = funkcje.find_position(numbers, search_value)

    if position != -1:
        print(f"Liczba {search_value} znajduje się na pozycji: {position}")
    else:
        print(f"Liczba {search_value} nie została znaleziona.")
    
    print(f"Najmniejsza liczba: {min_value}, na pozycji: {min_pos}")
    print(f"Największa liczba: {max_value}, na pozycji: {max_pos}")
    print(f"Średnia wartość wszystkich liczb: {avg_value}")

main()
