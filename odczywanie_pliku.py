with open('my_file.txt', 'r') as file1:
    # content = file1.read(5)
    # print(content)
    content = file1.read()
    # print(content)

# plik jest już zamkniety
print(content)

# policz liczbę unikalnych słów w pliku
print("Typ zmiennej przed użyciem split:", type(content))
# content = content.split() # konwersja stringa na liste przy separatorze spacji
content = content.lower().replace(',', '').replace('(', '').replace(')', '').replace('.', '').split()
print("Typ zmiennej po użyciu split:", type(content))
print(content)

# content = set(content)
print("Liczba słów w pliku to:", len(set(content)))


