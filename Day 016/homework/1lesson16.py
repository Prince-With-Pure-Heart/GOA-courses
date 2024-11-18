names = ["Aleqsandre", "Zura", "Nino", "Nikolozi", "Gabrieli"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[0])


numbers1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numbers1[0] = 1
numbers1[2] = 1
numbers1[4] = 1
numbers1[6] = 1
numbers1[8] = 1
numbers1[10] = 1
print(numbers1)


print(numbers[9])
surname = "Ghomidze"
for i in range(0, len(surname),):
    print(surname[i])


user_name = input("Enter your Username: ")
user_adress = input("Emter your adress: ")
user_surname = input("Enter your surname")
user_age = int(input("Enter your age: "))
user_info = [user_name, user_adress, user_surname, user_age]
print(user_info)