def get_number(input_number):
    n = input_number
    file = open(f'multiples{n}.txt', 'w')
    file.write(f'Multiples number of {n}\n')
    while n < 1000:
        file.write(f'{n}\n')
        n += input_number
    file.close()