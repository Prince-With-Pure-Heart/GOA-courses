#3) შექმენით ფუნქცია რომელსაც გადაეცემა სია შემდგარი სტრინგებისგან, გადაუარეთ ამ სიას და შეამოწმეთ თუ მისი characterების რაოდენობა არის ლუწი, ჩაამატეთ ეს კონკრეტული სიის ელემენტი ახალ ცარიელ სიაში და გადააკეთეთ იგი upper ფუნქციით, თუ იქნება ამ სტრინგის ასოების რაოდენობა კენტი, ჩაამატეთ ეს ელემენტი ახალ სიაში რომელსაც პირველი character ექნება გადიდებული, დანარჩენი პატარა. საბოლოოდ გამოიტანეთ ეს სია.
def changing_list(strings_list):
     
    changed_strings_list = []
    for i in strings_list:
           if len(i) % 2 == 0:
                 changed_strings_list.append(i.upper())
           elif len(i) % 2 != 0 :
                 changed_strings_list.append(i.capitalize())
    return changed_strings_list

print(changing_list(["ale", "luka", "giorgi", "jumberi", "shokoladiani blini"]))
                 

