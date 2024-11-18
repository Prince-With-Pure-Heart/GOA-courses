def equable_triangle(a,b,c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area == a + b + c
    

print(equable_triangle(int(input()), int(input()), int(input())))

# name = input("Enter your name: ")
# lastname = input("Enter your lastname: ")
# print(f"Your fullname is {name} {lastname}")git