def return_area(l,w):
    if l == w :
      return l * w
    else: 
       return  (2 * l) + (2 * w)

print(return_area(int(input()), int(input())))

