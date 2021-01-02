number = input("Enter Number: ")
counter = 0
numbers = []
s = 0
while number != '0':
    if number.isdigit():
        numbers.append(number)
        counter += 1
    number = input("Enter Number: ")
for n in numbers:
    s = s + int(n)

print(f"avreg of tour number{numbers}")
print(f"avrege of your numbers {s/counter}")