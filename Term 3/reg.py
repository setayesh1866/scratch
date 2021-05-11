def register(name, last, Brith, code):
    file = open('names.txt', 'a')
    file.write(f'{name}, {last}, {Brith}, {code}\n')
    file.close()