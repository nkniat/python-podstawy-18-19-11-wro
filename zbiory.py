digits = {0, 1, 2, 3, 4, 5, 6}
#print(digits[0]) #error

digits = {0, 1, 2, 3, 4, 5, 7, 0, 1, 2, 3, 4, 5, 6}
print(digits)

my_set = {"mama", "pies", False, True, 2, 5, 0, 1}
print(my_set)

my_tuple = (1, 2, 3, 5, 6, 6, 6, True, False, "Myszka")
print(my_tuple)
my_set2 = set(my_tuple)
print(my_set2)

#body = {'head', ['left hand', 'right hand'], 'belly'} #error - element mutowalny wśrodku
body = {'head', ('left hand', 'right hand'), 'belly'}

if 'head' in body:
    print("Masz łep na karku")

len(my_set2)

letters1 = {'a', 'b', 'c'}
letters2 = {'b', 'c', 'd', 'e'}

# operacje na zbiorach
print(letters1.union(letters2)) # suma
suma = letters1 | letters2
print("suma:", suma)

print(letters1.intersection(letters2)) # czesc wspolna
wspolna = letters1 & letters2
print("Czesc wspolna:", wspolna)

print(letters1.difference(letters2)) # 1 - 2
roznica = letters1 - letters2
print("roznica:", roznica)

print(letters1.symmetric_difference(letters2)) # róznica symetryczna
roznica_symetryczna = letters1 ^ letters2
print("Roznica symetryczna:", roznica_symetryczna)

# zbior jest edytowalny
letters1.update({'g', 'h'})
print(letters1)
letters1.add('i')
print(letters1)
letters1.remove('a')
print(letters1)
