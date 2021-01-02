morse = {
'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', ' ' : ' ', 
'Y':'-.--', 'Z':'--..'
}

text = input('enter ur text: ')
translate = ''
for chracter in text:
    translate += morse[chracter.upper()] + ''
print(translate)

