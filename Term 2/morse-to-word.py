def get_morse(string):
    words = string.split('   ')
    transl = ''
    for words in words:
        for chracter in words.split():
            transl += morse[chracter]
        transl += ' '
    return transl

morse = { 
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        ' ':' '}

ink = input('Enter your morce code: ')
text = get_morse(ink)
print(transl)