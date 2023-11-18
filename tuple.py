#tworzenie tupli:
my_tuple = (1, 2, 3, 5, 6, 6, 6, True, False, "Myszka")

# tupla na bazie listy
listaMieszana = ["mama", 0, True, 2.5, -5, ["Ala ma kota", "Ola ma psa"]]
my_tuple2 = tuple(listaMieszana)

print("Lista:", listaMieszana, "a jej typ to:", type(listaMieszana))
print("Tupla:", my_tuple2, "a jej typ to:", type(my_tuple2))

print(my_tuple2[5])
print(len(my_tuple2))
my_tuple2[5].append("Jasiu ma rybki")
print(my_tuple2)
print(len(my_tuple2))

my_big_tuple = my_tuple + my_tuple2
print(my_big_tuple)

print(my_tuple * 30)

print("Liczba 6 w tupli:", my_tuple.count(6))
print(my_tuple.index(5))
print(len(my_big_tuple))

i = 1
for element in my_big_tuple:
    print(i, ":", element)
    i += 1

