#1) შექმენით სია სადაც გექნებათ მოცემული 5 სახელი, index ების გამოყენებით დაბეჭდეთ ცალცალკე, dont use for cycle
names = ["Gio", "Luka", "Dato", "Nika", "Jeko"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

#2) შექმენით სია სადაც გექნებათ მოცემული 5 სახელი, for ციკლის გამოყენებით კი დაბეჭდეთ თითოეული
people = ["Aleksandre", "Ioane", "ELene", "Zura", "Qeta"]
for i in range(0, len(people)):
    print(people[i])

#3) შექმენით სია სადაც გექნებათ 1-10 ჩათვლი რიცხვები, for ციკლის გამოყენებით დაბეჭდეთ არ რიცხვების ჯამი ცალკე და ნამრავლი ცალკე
numbers = [1,2,3,4,5,6,7,8,9,10]
result = 0 
multiple = 1
for i in numbers:
    result = result + i
    print(result)

for i in numbers:
    multiple = multiple * i
    print(multiple)

#4) შექმენით სია სადაც გექნებათ 1-10 ჩათვლით რიცხვები, for ციკლის გამოყენებით დაბეჭდეთ მხოლოდ ლუწი რიცხვები და მათი ჯამი
ages = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in ages:
    if i % 2 == 0:
        sum = sum + i
        print(sum)
    
#5) შექმენით სია სადაც გექნებათ 1-10 ჩათვლით რიცხვები, for ციკლის გამოყენებით დაბეჭდეთ მხოლოდ კენტი რიცხვების ჯამი და ნამრავლი
prices = [1,2,3,4,5,6,7,8,9,10]
odd_numbers_result = 0
odd_numbers_multiple = 1
for i in prices:
    if i % 2 == 1:
        odd_numbers_result = odd_numbers_result + i
        print(odd_numbers_result)
        odd_numbers_multiple = odd_numbers_multiple * i
        print(odd_numbers_multiple)

#6) შექმენით სტრინგი და გამოიტანეთ for ციკლის მეშვეობით ყველა სიმბოლო
sport = "basketball"
for i in range(0, len(sport)):
    print(sport[i])

#7)შექმენით სტრინგი და for ციკლის გამოყენებით შეართეთ მხოლოდ ის სიმბოლოები რომლებიც არიან ლუწ ინდექსებზე
subject = "science"
even_indexes_string = ""
for i in range(0, len(subject)):
    if i % 2 == 0:
        even_indexes_string += subject[i]
        print(even_indexes_string)

