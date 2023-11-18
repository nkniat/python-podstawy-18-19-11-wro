# listy
# listy są uporządkowane
# w listach są indexy
# w listach mogą być powtórzenia
# lista jest mutowalna (da się są edytować)

# tworzymy pustą liste
lista = []
print(lista)

listaLiczb = [1, 2, 2.5, 5, -1, -5, -10.5, 1]
listaMieszana = ["mama", 0, True, 2.5, -5, ["Ala ma kota", "Ola ma psa"]]
listaStringow = ["kajak", "mama", "axa", "myszka"]

print(listaLiczb[5])
# odwolanie do ostatniego elementu
print(listaMieszana[-1])
# odwolanie do zagniezdzonej listy w liscie
print(listaMieszana[-1][0])

print("Dodawanie do listy")
lista = ["tata"]
print(lista)
#lista.append(["mama", "babcia"])
lista.append("mama")
print(lista)
lista = lista + ["córka", "druga córka"]
print(lista)
lista.extend(["brat", "drugi brat"])
print(lista)

lista.insert(2, "babcia")
print(lista)

# sortowanie
print(listaLiczb)

listaLiczb.sort(reverse=True)
print(listaLiczb)

print(max(listaLiczb))
print(min(listaLiczb))

# ile razy wystepuje dany element
print(listaLiczb.count(1))

# usuwanie elementow z listy
print(lista.pop())
print(lista)

# usuwa pierwsze wystapienie elementu w liscie
print(listaLiczb.remove(1))
print(listaLiczb)

# print(lista.clear())
# print(lista)

# usuwanie elementu
del lista[-1]
print(lista)
