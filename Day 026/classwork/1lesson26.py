# 1) შექმენით ფუნქცია, რომელსაც გადაეცემა ორი რიცხვი: start, end. ფუნქციამ უნდა დაბეჭდოს მათ შორის არსებული რიცხვები range-ის გამოყენებით
def count_numbers(start, end):
    for i in range(start, end):
        print(i)

count_numbers(int(input("Please enter your number: ")), int(input("Please enter your number: ")))

# 2) შექმენით ფუნქცია, რომელსაც გადაეცემა start, end. ამ შემთხვევაში გამოთვალეთ მათ შორის არსებული რიცხვების ჯამი
def sum(start, end):
    for i in range(start, end):
        start += i 
        print(start)

sum(int(input("Please enter your first number: ")), int(input("Please enter your second number: ")))

# 3) შექმენით ფუნქცია, რომელსაც გადაეცემა start, end. ამ ორ რიცხვს შორის არსებული, ყველა დაამატეთ ახალ სიაში. საბოლოოდ დაბეჭდეთ სიის საშუალო არითმეტიკული
def list_add(start, end):
    list = []
   
    for i in range(start, end):
        list.append(i)
      
        print(list)
       


list_add(int(input("Please enter your first number: ")), int(input("Please enter your second number: ")))

#  4) შექმენით ფუნქცია, რომელსაც გადაეცემა სახელი და ინდექსი. თქვენი დავალებაა, რომ სახელის ინდექსზე მყოფი ასო დაბეჭდოთ
def print_index(name, index):
     print(name[index])

print_index(input("Please enter your name: "), int(input("Please enter your number: ")))
         

#  bonus
def ages():
    for age in range(100):
        if age >= 18 and age < 60:
            print("You are adult")
        elif age >= 60 and age < 100:
            print("You are old")
        elif age == 100:
            print("you are very old")
        
ages()
     
        
