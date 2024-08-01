#1)  შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვების სია. თქვენი დავალებაა, რომ ამ სიის ლუწ ინდექსებზე მყოფი რიცხვების ჯამი დააბრუნოთ. აუცილებლად გამოიყენეთ return ამ და ასევე შემდეგ დავალებებში.
def sum(list):
    result = 0
    for i in range(len(list)):
        if i % 2 == 0:
           result += list[i]
    return result
        
print(sum([1,2,3,4,5,6,7,8,9,10]))

#2) შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. თქვენი დავალებაა, რომ დააბრუნოთ ამ სიის განახლებული ვერსია, სადაც ყველა სახელი დიდი ასოთი დაიწყება.
def capitalized_names(names_list):
    changed_list = []
    for name in names_list:
        changed_list.append(name.capitalize())
    return changed_list

print(capitalized_names(["alex", "luka"]))


#3)შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვი. თქვენი დავალებაა, რომ დააბრუნოთ ლუწია თუ კენტი ის.
def even_or_odd(num):
    if num % 2 == 0:
        return ("Your number is even")
    else:
        return ("Your number is odd")
    
print(even_or_odd(int(input("Please enter your number: "))))
           

# 4) შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვების სია. შემდეგ გამოიყენეთ ციკლი, რათა განიხილოთ ამ სიის ყველა რიცხვი - თუ რიცხვი ლუწია, ახალ სიაში დაამატეთ მისი განაყოფი ორზე, ხოლო თუ კენტია, მაშინ რიცხვის ნამრავლი ორზე. საბოლოოდ დააბრუნეთ განახლებული სია/
def list():
    num_list = [1,2,3,4,5,6,7,8]
    new_list = []
    for num in num_list:
        if num % 2 == 0:
            new_list.append(num // 2)
        else:
            new_list.append(num * 2)
    return new_list

print(list())

#5) შექმენით ფუნქცია, რომელიც დააბრუნებს მარტივია თუ არა რიცხვი (მარტივია რიცხვი, თუ მას მარტო ორი გამყოფი აქვს).
def check_if_prime(num):
    if num == 2:
        return str(num) + " is prime"
    if num <= 1:
        return str(num) + " is invalid number"
    
    count = 2
    
    for i in range(2, num):
        if num % i == 0:
            count = count + 1
        if count > 2:
            return str(num) + ' is not prime'
    
    return str(num) + ' is prime'

print(check_if_prime(int(input("Please enter your number: "))))