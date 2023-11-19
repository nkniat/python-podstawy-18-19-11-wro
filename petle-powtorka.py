wynik = 0
licznik = 0

# while licznik < 3:
#     x = float(input("podaj DODATNIA liczbe "))
#     if x >= 0:
#         wynik += x
#     else:
#         print("Hej, podałeś liczbę ujemną!")
#         #break  # ucieczka z pętli
#         continue  # pomija jedną iterację pętli
#     print("Aktualny wynik to: ", wynik)
#     licznik += 1

for i in range(3):
    x = float(input("podaj DODATNIA liczbe "))
    if x >= 0:
        wynik += x
    else:
        print("Hej, podałeś liczbę ujemną!")
        #break  # ucieczka z pętli
        continue  # pomija jedną iterację pętli
    print("Aktualny wynik to: ", wynik)
