num = int(input("Please enter your number: "))
if num > 0:
    print("Your number is positive")
elif num < 0:
    print("Your number is negative")
else:
    print("Your number equals to zero")

user_age = int(input("Please enter your age: "))
if user_age >= 0 and user_age < 18:
    print("You are child")
elif user_age >= 18 and user_age < 50:
    print("You are adult")
else:
    print("you are old")