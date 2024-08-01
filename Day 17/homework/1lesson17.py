#1) შექმენით სია სადაც გექნებათ მოცემული 5 სახელი, index ების გამოყენებით დაბეჭდეთ ცალცალკე, dont use for cycle
names = ["Gio", "Nika", "Luka", "Gabo", "Ioane"]
print(names[0], names[1], names[2], names[3], names[4])

#2) შექმენით სია სადაც გექნებათ მოცემული 5 სახელი, for ციკლის გამოყენებით კი დაბეჭდეთ თითოეული
usernames = ["Aleqsandre", "Mari", "Lazare", "Anri", "Elene"]
for i in range(0, len(usernames)):
    print(usernames[i])

#3) შექმენით სია სადაც გექნებათ 1-10 ჩათვლი რიცხვები, for ციკლის გამოყენებით დაბეჭდეთ არ რიცხვების ჯამი ცალკე და ნამრავლი ცალკე
sum = 0
multiple = 1
numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    sum = sum + num
    print(sum)

for num in numbers:
    multiple = multiple * num
    print(multiple)
  
#4) შექმენით სტრინგი და გამოიტანეთ for ციკლის მეშვეობით ყველა სიმბოლო
info = "Goa"
for i in  range(0, len(info)):
    print(info[i])
    
#5) შექმენით სტრინგი  და for ციკლის გამოყენებით შეართეთ მხოლოდ ის სიმბოლოები რომლებიც არიან ლუწ ინდექსებზე
user_name = "Aleqsandre"
even_index_string = ""
for i in range(0, len(user_name), 2):
     if i % 2 == 0:
          even_index_string = even_index_string + user_name[i]
          print(even_index_string)

#6) შექმენით სია სადაც გექნებათ 1-10 ჩათვლით რიცხვები, for ციკლის გამოყენებით დაბეჭდეთ მხოლოდ ლუწი რიცხვები და მათი ჯამი
prices = [1,2,3,4,5,6,7,8,9,10]
sum1 = 0
for num in prices:
    if num % 2 == 0:
        sum1 = sum1 + num
        print(sum1)
    

#7) შექმენით სია სადაც გექნებათ 1-10 ჩათვლით რიცხვები, for ციკლის გამოყენებით დაბეჭდეთ მხოლოდ კენტი რიცხვების ჯამი და ნამრავლი
container = [1,2,3,4,5,6,7,8,9,10]
sum2 = 0
multiple1= 1

for num in container:
    if num % 2 == 1:
        sum2 = sum2 + num
        multiple1 = multiple1 * num

        print(sum2)
        print(multiple1)
         


    
 