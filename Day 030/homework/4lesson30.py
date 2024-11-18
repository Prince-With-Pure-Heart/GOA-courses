#4) შექმენით ფუნქცია რომელსაც გადაეცემა სია შემდგარი ყველანაირი სტრინგისგან (დიდი ასოებით / პატარა ასოებით : "vano" , "LUKA") , გადაურეთ ამ სიას და თუ ეს კონკრეტული ელემენტი არის შემდგარი დიდი ასოებისგან, დაამატეთ სიაში ისე როგორც lower, ხოლო თუ შედგება პატარა ასოებისგან დაამატეთ სიაში ისე როგორც upper / !HINT : გადახედეთ ფუნქციებს, isupper() და islower()!
def different_lists():
    list_of_strings = ["vano", "LUKA", "SHOKOLADIANI BLINI", "nugari"]
    new_list = []
    for i in list_of_strings:
        if i.isupper():
            new_list.append(i.lower())
            
        elif i.islower():
            new_list.append(i.upper())
           
    return new_list

print(different_lists())

