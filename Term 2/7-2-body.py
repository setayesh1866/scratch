print("***BMI***")

h = float(input("Whats your hight?(meter): "))
w = float(input("Whats your wight?(kg): "))

BMI = w / (h*h)

print(f"your body mass index is: {BMI:.2f} ")

if BMI < 18.5:
    print("You are UNDERWEIGHT!")

elif 18.5 <= BMI and BMI <= 24.9:
    print("You are NORMAL")

elif 25 <= BMI and BMI <= 29.9:
    print("You are OVERWEIGHT!")

elif 30 <= BMI and BMI <= 34.9:
    print("You are OBESE!")

elif BMI >= 35:
    print("You are EXTREMELY OBSES!")
    