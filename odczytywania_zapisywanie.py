imionaNazwiskaRazem = []

with open('imiona_nazwiska.txt', 'r', encoding='UTF-8') as plik_txt:
    for linia in plik_txt:
        imionaNazwiskaRazem.append(tuple(linia.split()))

# imionaNazwiskaRazem = [
#     ('Elżbieta', 'Podsiadła'),
#     ('Edmund', 'Rezmer'),
#     ('Jan', 'Kawiak'),
#     ('Oskar', 'Koszela')
#  ]
# print(imionaNazwiskaRazem[0][1])

print(imionaNazwiskaRazem)
print("Imię: ", imionaNazwiskaRazem[15][0])
print("Nazwisko: ", imionaNazwiskaRazem[15][1])

with open('imiona.txt', 'w', encoding='UTF-8') as plik_txt:
    for element in imionaNazwiskaRazem:
        plik_txt.write(element[0] + '\n')

with open('nazwiska.txt', 'w', encoding='UTF-8') as plik_txt:
    for element in imionaNazwiskaRazem:
        plik_txt.write(element[1] + '\n')
