num = int(input("Please enter your number: "))
if num > 0:
    print("Your number is positive")
elif num < 0:
    print("Your number is negative")
else:
    print("Your number equals to zero")

for i in range(2,101,2):
    print(i)


Day = input("Enter any number 1-7: ")
if Day == 1:
    print("It's monday")
elif Day == 2:
    print("It's tuesday")
elif Day == 3:
    print("It's wednesday")
elif Day == 4:
    print("It's thursday")
elif Day == 5:
    print("It's friday")
elif Day == 6:
    print("It's saturday")
else:
    print("It's sunday")


user_num = int(input("Please enter your number: "))
if user_num % 2 == 0 and user_num > 0:
    print("Your number is even")
elif user_num % 2 == 1:
    print("Your number is odd")
else:
    print("your number equlas to zero")

for i in range(1,51):
    print(i)

num1 = int(input("Please enter your number: "))
if num % 3 == 0:
    print("fizz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")