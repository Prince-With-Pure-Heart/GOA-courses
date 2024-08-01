def filter_list(l):
   new_l = []
   for char in l:
        if type(char) == int:
            new_l.append(char)
   return new_l
            
print(filter_list([1, "123" , 2]))

# or
def filter_list(l):
   return [x for x in l if type(x) is not str]

print(filter_list([1, "123" , 2]))