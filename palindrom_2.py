# Podejście 2 - pythonowe
# slowo = "Natalia"
# print(slowo[::-1])

listaSlow = ["kajak", "mama", "axa", "myszka"]

for slowo in listaSlow:
    print("\nSłowo, które sprawdzam to: ", slowo)
    slowo_od_konca = slowo[::-1]
    if slowo_od_konca == slowo:
        print("Słowo", slowo, "jest palindromem")
    else:
        print("Słowo", slowo, "NIE jest palindromem")

# sprawdź czy zdanie jest palindromem ignorując spacje
# listaZdan = ["Ewo, żeby tu były buty beżowe", "Mer kilowy woli krem"]