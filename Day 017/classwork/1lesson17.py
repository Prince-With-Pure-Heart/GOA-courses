user_name = input("Enter your full name: ")
for i in range(0, len(user_name)):
    print(user_name[i])


name = input("Enter your full name: ")
for i in range(0, len(name), 2):
    print(name[i])
     
list = [1,2,3,4,5,6,7,8,9,10,11]
if 5 in list:
    print("Yes 5 is in your list")
else:
    print("No it's not")


numbers = [1,2,3,4,5,6,7,8,9,10]
result = 0
for num in numbers:
    if num % 2 == 0:
        result = result +2
        print(result)
