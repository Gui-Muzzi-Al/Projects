number = input("Digit a number")

if number.isdigit():
    number = int(number)
    if number % 2 == 0:
        print(f"This {number} is even")
    else:
        print(f"this {number} is odd")
else:
    print("You didn't insert an interger number")
