# program, który wyświetli menu dla użytkowania,
# użytkownik ma do wyboru kilka opcji: Dodaj zadanie, wyświetl zadania, usuń zadanie, zakończ program
# po wybraniu danej opcji, program wykonuje daną czynność

ToDo = []

while True:
    print("======= Menu ======= ")
    print("1. Dodaj zadnie")
    print("2. Wyświelt zadania")
    print("3. Usuń zadanie")
    print("4. Zakończ")

    wybor = input("Wybierz opcję z menu ")

    if wybor == "1":
        zadanie = input("Podaj nazwę zadania ")
        ToDo.append(zadanie)
        print("Zadanie dodane")
    elif wybor == "2":
        # wyświetl zadania >> ładnie wyświetl zadania (w formie listy, jedno zadnie pod drugim)
        print("Twoje zadania to:", ToDo)
    elif wybor == "3":
        # usuń zadanie
        co_usunac = int(input("Podaj index zadania do usuniecia "))
        del ToDo[co_usunac - 1]
        # zad dom. przed usuwaniem lepiej wyswietlic cala liste zadań
    elif wybor == "4":
        # wyświetl zadania
        break
    else:
        print("Nie rozumiem komendy")
