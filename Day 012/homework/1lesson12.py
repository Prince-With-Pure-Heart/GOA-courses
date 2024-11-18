# მომხმარებელს ჯერ შემოატანინეთ ბიუჯეტი, შემდეგ კი ის თანხა, რომელიც სასურველი ნივთის საყიდლად სჭირდება. დაბეჭდეთ შეუძლია ყიდვა თუ არა.
user_budget = int(input("Enter your budget: "))
price = int(input("Enter price: "))
if user_budget >= price:
    print("You can buy a product")
else:
    print("Sorry you can't buy a product ")


# შექმენით ცვლადი, სადაც შეინახავთ თქვენთვის სასურველ პაროლს. მომხმარებელს შეეკითხეთ პაროლი და სანამ სწორს არ შემოიტანს თავიდან შეეკითხეთ, თან დაუმატეთ თუ მერამდენე ცდაზეა (გამოიყენეთ while ციკლი). თუ მან მეხუთე ცდაზეც ვერ შეიყვანა სწორად, დაუპრინტეთ, რომ სისტემა დაბლოკილია.
registered_password = "Aleks123456"
password = input("Please enter your password: ")

while password != registered_password:
    password = input("Please enter your password again: ")
if password == registered_password:
    print("You have granted acces to your account.")

# მომხმარებელს შეეკითხეთ for ციკლისთვის მინიმალური, მაქსიმალური მნიშვნელობები და step-ის რიცხვი. ამ მნიშვნელობებით მოახდინეთ ციკლის მუშაობა და დაპრინტეთ თითოეული რიცხვი.
min_num = int(input("Enter your number: "))
max_num = int(input("Enter your number: "))
step_num = int(input("Enter your number:"))
for i in range(min_num,max_num, step_num ):
    print(i)

#მომხმარებელს შემოატანინეთ სამკუთხედის სამი გვერდი და შეამოწმეთ თუ არსებობს ის. არსებობის შემთხვევაში დაპრინტეთ, რომ მონაცემები სწორია, სხვა შემთხვევაში შემოატანინეთ გვერდების მნიშვნელობები თავიდან ( გამოიყენეთ while ციკლი ).
# მომხმარებელს შეეკითხეთ წელი და და დაპრინტეთ ნაკიანია ის თუ არა.
user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("You can take part in elections")
else:
    print("You can't")



#მომხმარებელს შემოატანინეთ რიცხვი და შეამოწმეთ თუ არის როგორც ორის, ასევე სამის ჯერადი. არსებობის შემთხვევაში დაპრინტეთ ეს რიცხვი, ხოლო თუ არ იქნება მაშინ თავიდან შეეკითხეთ (გამოიყენეთ while ციკლი).
s1 = int(input("Please enter your first side:"))
s2 = int(input("Please enter your second side:"))
s3 = int(input("Please enter your third side:"))
is_valid = (s1 + s2 > s3 ) and (s2 + s1 > s3) and (s3 + s2 > s1)
while is_valid != True:
    s1 = int(input("Please enter your first side:"))
    s2 = int(input("Please enter your second side:"))
    s3 = int(input("Please enter your third side:"))

#შექმენით კალკულატორი, სადაც მომხმარებელი აირჩევს შემდეგ ოპერაციებს: + - * / და მის მიერ შემოტანილი ორი რიცხვით მიიღებს პასუხს.
operation = input("Please enter operation (+ - * /) :")
number1 = int(input("please enter your first number: "))
number2 = int(input("Please enter your second number: "))
if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
    
num1 = int(input("Enter your number: "))
while num1 % 2 == 0 and num1 % 3 == 0:
    print(num1)
if num1  % 2 != 0 and num1 % 3 != 0:
    print(input("Try agin:"))


#მომხმარებელს შეეკითხეთ წელი და და დაპრინტეთ ნაკიანია ის თუ არა.
year = int(input("Enter yaer:"))
if year % 4 == 0:
    print(year)






