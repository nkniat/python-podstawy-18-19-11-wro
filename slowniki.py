# słownik - para klucz i wartość
person = {
    'Name': 'Natalia',
    'Age': 36,
    'Height': 170
}

# print(person[0]) # error
print(person['Name'])
#print(person['Email']) #Error
print(person.get('Age'))
print(person.get('Email', 0))

digist = {
    0: 'zero',
    1: 'jeden',
    2: 'dwa'
}
print(digist[0])

# klucz nie może być modyfikowalny
# cars = {
#     ["Toyota", "Yaris"]: "KRA12345",
#     ["Toyota", "Aygo"]: "KRA52345"
# }
# print(cars)

cars = {
    ("Toyota", "Yaris"): "KRA12345",
    ("Toyota", "Aygo"): "KRA12345"
}
print(cars)

cars = {
    ("Toyota", "Yaris"): "KRA12345",
    ("Toyota", "Yaris"): "KRA52345"
}
print(cars) # NOK - klucz się nadpisał

cars = {
    ("Toyota", "Yaris"): "KRA12345",
    ("Toyota", "Corolla"): "KRA12345"
}
print(cars) # OK - klucze są unikalne, ale wartosci mogą być takie same

person['Email'] = "natalia@merito.pl"
print(person)
person['Email'] = "nati@merito.pl"
person['Age'] = "37"
print(person)

digist.update({3: 'trzy', 4: 'cztery'})
print(digist)

#del person['Email']
#print(person)

if 3 in digist:
    print("3 jest opisane")

if 5 not in digist:
    print("5 nie jest opisane")

print("Długość słownika:", len(digist))

print("Klucze w słowniku: ", person.keys())
print("Wartosci w słowniku: ", person.values())
print("Elementy w słowniku: ", person.items())

a = 1
b = 2
c = 3
print(a, b, c)

a, b, c = 4, 5, 6
print(a, b, c)

for key in person:
    print("Klucz: ", key)

for value in person.values():
    print("Wartość: ", value)

for key, value in person.items():
    print("Klucz:", key, "ma wartosc: ", value)
