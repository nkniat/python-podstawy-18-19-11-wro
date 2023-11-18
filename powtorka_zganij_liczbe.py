szukanaLiczba = 13
zgadywanaLiczba = 0

while zgadywanaLiczba != szukanaLiczba:
    zgadywanaLiczba = int(input("Odgadnij, o jakiej liczbie myślę: "))

    if zgadywanaLiczba == szukanaLiczba:
        print("Brawo! Zgadłeś")
    elif zgadywanaLiczba < szukanaLiczba:
        print("Twoja liczba jest za mała")
    elif zgadywanaLiczba > szukanaLiczba:
        print("Twoja liczba jest za duża")

# Ułatw użytkownikowi zgadywanie i podaj zakresy, w jakich sie obraca, np.:
#  20 >> print("Nowy przedział to: ") (nieskonczonosc, 20)
#  10 >>  print("Nowy przedział to: ") (10, 20)

# Ogranicz użytkownikowi liczbę prób do np. 10.
# liczbaProb = 10
# jeśli nie zgdałeś, to liczbaProb = liczbaProb - 1
