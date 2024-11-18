#1) მომხმარებელს შემოატანინეთ სიტყვა და შეამოწმეთ არის თუ არა ის პალინდრომი. პალინდრომი არის სიტყვა, რომელიც შებრუნებულიც ზუსტად იგივე გამოდის - radar, level, rotor. ამ დავალებისთვის გამოიყენეთ ციკლი და indexing.
word = "kayak"
reversed_word = ""
for index in range(len(word) - 1, -1, -1):
    reversed_word = reversed_word + word[index]

if word == reversed_word:
    print(word, "is palindrome")
else:
    print(word, "is not palindrome")

#2) მომხმარებელს შემოატანინეთ ხუთი რიცხვი და შეიტანეთ ისინი სიაში. შემდეგ თქვენ უნდა იმუშაოთ ამ სიაზე: თუ რომელიმე ელემენტი სიაში ორჯერ მეორდება, დაამატეთ ის ახალ სიაში. საბოლოოდ გექნებათ ორი ვარიანტი: ცარიელი ახალი სია / ახალი სია სადაც იქნება მინიმუმ ერთი ელემენტი. თუ სია ცარიელი იქნება, დაბეჭდეთ რომ სია ცარიელია. სხვა შემთხვევაში დაბეჭდეთ ახალი სია.
numbers_list = []
repeat_value = []
for i in range(5):
    num = int(input("please enter your number: "))
    numbers_list.append(num)

for numbers in numbers_list:
    count = numbers_list.count(numbers)
    print(count)

for numbers in numbers_list:
    count = numbers_list.count(numbers)
    if count > 1 and numbers not in repeat_value:
        repeat_value.append(numbers)
        print(repeat_value)

#3)ომხმარებელს შემოატანინეთ ხუთი სიტყვა. თქვენი დავალებაა, რომ ააწყოთ ახალი სიტყვა - თითოეულის პირველი ასო დაამატოთ მას. საბოლოოდ კი დაბეჭდოთ ეს სიტყვა.
string1 = "Luka"
string2 = "Ball"
string3 = "Word"
string4 = "Lzare"
string5 = "String"
print(string1[0] + string2[0] + string3[0] + string4[0] + string5[0])

