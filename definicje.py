"""
Napisac program, który pozwoli użytkownikowi:
1. dodawać nowe definicje
2. szukać istniejących definicji
3. usuwać wybrane definicje
"""

#utworzenie pustegoo słownika
definicje = {}

while True:
    print("1. Dodaj definicje")
    print("2. Znajdź definicje")
    print("3. Usuń definicje")
    print("4. Wyświetl wszystkie definicje") # W domu
    print("5. Zakończ")

    wybor = input("Co chcesz zrobić? ")

    if wybor == "1":  # dodaj definicję
        klucz = input("Podaj słowo do zdefiniowania ")
        definicja = input("Podaj definicję słowa: ")
        definicje[klucz] = definicja
        print("Definicja została dodana\n")
    elif wybor == "2":  # wyświetl definicję
        klucz = input("Jakiego słowa szukasz? ")
        if klucz in definicje:
            print(klucz, "to", definicje[klucz], "\n")
        else:
            print("Nie mam tej definicji \n")
    elif wybor == "3":  # usuwanie
        klucz = input("Jakie słowo chcesz usunąć?")
        if klucz in definicje:
            del definicje[klucz]
            print("Definicja została usunięta!\n")
        else:
            print("Nie mam tej definicji \n")
    elif wybor == "4":  # wyświetl wszystkie definicje
        pass
    elif wybor == "5":
        break
    else:
        print("Nie rozumiem komendy :(")
