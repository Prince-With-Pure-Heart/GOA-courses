# 1) შექმენით ფუნქცია, რომელსაც გადაეცემა სტრინგი და დააბრუნეთ ეს სტრინგდი შებრუნებულ + დიდი ასოებით (reversed / upper).
def reversed_uppercased_string(str):
     return str[::-1].upper()
          


print(reversed_uppercased_string(input("Enter anything: ")))