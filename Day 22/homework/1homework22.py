#1. მომხმარებელს შემოატანინეთ ნებისმიერი სიტყვა. თუ მისი სიგრძე აღემატება სამს, დაბეჭდეთ მისი პირველი სამი ასო. ხოლო თუ ნაკლებია ან ტოლი სამის, დაბეჭდეთ სიტყვის პირველი ასო.
word = input("Please enter any word: ")
if len(word) > 3:
    print(word[0:3])
else:
    print(word[0])  

#2. for ციკლით შექმენით 10-იდან 20-ის ჩათვლით არსებული მთელი რიცხვების სია. შემდეგ გამოიყენეთ slicing, სადაც სტეპი იქნება 2-ის ტოლი.
num_list = []
for i in num_list:
    num_list.append(i)


#3. მომხმარებელს შემოატანინეთ სიტყვა. შემდეგ გამოიყენეთ ნასწავლი მასალა და შეაბრუნეთ ის.
string = input("Please enter any string value: ")
i = len(string)
step = -1
result = 0
while i > result:
    i = i + step
    print(string[i])