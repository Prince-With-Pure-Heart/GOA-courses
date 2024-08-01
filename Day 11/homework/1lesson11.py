for i in range(1, 51):
    if i % 5 == 0:
      print(i)


for i in range(2,21):
    if i % 2 ==0:
        print(i)
    
final_product = 1
for i in range(5,11):
    final_product= final_product * i
    print(final_product)
    
user_num = int(input("enter a number:"))
product = 1
for i in range(1,user_num + 1):
    product*=i
    print(product)


user_num1 = int(input("enter a number:"))
if user_num1 % 2 == 0:
    user_num1/=2
    print(user_num1)
else:
    user_num1*= 3+1
    print(user_num1)

i = 10
while i > 0:
    print(i)
    i-=1

user_nickname= input("Eter a nickname /or/ quit:" )
while user_nickname!= "quit":
    user_nickname = input("Enter a nickname /or/ quit:")

start =10
finish =21
while start < finish:
    if start % 2 == 0:
        print(start)
    start +=1


i = 1
while i <= 10:
    print(i**2)
    i+=1
     
    
num = int(input("Enter your number: "))
if num < 0:
    print("Try again ")
elif num >=0:
    print("You succesed")

result = 10
while result > 0:
    print(result)
    result= result - 1

name = input("Enter yor name: ")

