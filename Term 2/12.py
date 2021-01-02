number = input("Enter your number: ")
counter = 0
nembers = []
s = 0
while number != '0':
    if number.isdigit():
        numbers.append(number)
    number = input("Enter your number: ")
    counter += 1
for n in numbers:
    s = s + int(n)
print(numbers)
print(s)
print(f"you entered {counter} number.")
