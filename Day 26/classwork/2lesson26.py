#6) შექმენით ფუნქცია, რომელსაც გადაეცემა ორი რიცხვი. საბოლოოდ ფუნქციამ უნდა დააბრუნოს ამ ორი რიცხვის ჯამი, ფუნქციის გარეთ დაბეჭდეთ ეს შედეგი
def sum(num0, num1):
    return   num0 + num1

print(sum(int(input("Please enter first number: ")), int(input("Please enter second number: ")) ))
 


#7) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. თქვენი დავალებაა, რომ დააბრუნოთ სიაში არსებული რიცხვების ჯამი, ასევე დაბეჭდოთ ის ფუნქციის გარეთ
def list():
    num_list = []
    for i in  range(10):
        num_list.append(i)

    return num_list

print(list())


#8) შექმენით ფუნქცია, რომელსაც გადაეცემა სახელი. თქვენი დავალებაა, რომ ახალ სთრინგში დაამატოთ ლუწ ინდექსიანი ასოები სახელიდან. ეს შედეგი დააბრუნებინეთ ფუნქციას, ასევე დაბეჭდეთ ფუნქციის გარეთ
def name():
    name = input("Please enter your name: ")
    even_index_name = name[::2]

    return even_index_name

print(name())