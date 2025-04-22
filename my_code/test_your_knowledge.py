#  Exercise
#  Ask the user to enter their name
#  Ask the user to enter their age
#  If name and age are entered:
#      Display:
#          Your name is {name}
#          Your name reversed is {reversed name}
#          Your name contains (or does not contain) spaces
#          Your name has {n} letters
#          The first letter of your name is {letter}
#          The last letter of your name is {letter}
#  If nothing is entered in name or age:
#      Display "Sorry, you left some fields empty."


name = input("Whats your name: ")
age = input("How old are you: ")
reversed_name = name[::-1]
range_name = len(name)

if name and age:
    print(
        f"your name is, {name}, your age is, {age},"
        f" your reversed name is {reversed_name}, "
    )
    if " " in name:
        print("Your name have spaces")
    else:
        print("Your name don`t have spaces")

    print(
        f"your name contains {range_name} letters, "
        f"your first letter is {name[0]}, "
        f"your last letter is {name[-1]}, "
    )
else:
    print("Sorry, you left some fields empty.")
