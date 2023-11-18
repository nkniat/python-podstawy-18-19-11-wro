listaSlow = ["kajak", "mama", "axa", "myszka"]

for slowo in listaSlow:
    print("\nSłowo, które sprawdzam to: ", slowo)

    # print("Piersza litera: ", slowo[0])
    # print("Druga litera: ", slowo[1])
    # print("Trzecia litera: ", slowo[2])

    # if slowo[0] == slowo[-1]:
    #     print("Pierwsza i ostatnia litera jest taka sama")
    # else:
    #     print("Pierwsza i ostatnia litera jest różna")

    # liczba iteracji to długość dlanego słowa /2 - ale bez reszt
    liczbaIteracji = len(slowo) // 2
    # liczbaIteracji = int(len(slowo) / 2)

    flaga_czy_palindrom = True

    # pętla, któa 'chodzi' po danym słowie z listy
    for i in range(liczbaIteracji):
        if slowo[i] != slowo[-1 - i]:
            print("Litera", slowo[i], "nie zgadza się")
            # print("Slowo", slowo, "nie jest palindromem")
            flaga_czy_palindrom = False
            break
        else:
            print("Litera", slowo[i], "jest w porządku")

    if flaga_czy_palindrom:
        print("Słowo", slowo, "jest palindromem")
    else:
        print("Słowo", slowo, "nie jest palindromem")
