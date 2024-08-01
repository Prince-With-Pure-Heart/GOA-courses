#1
numbers = []
start = 0
end = 14 + 1
step = 3
while start < end:
    numbers.append(start)
    start = start + step
    print(numbers)

#2
names = ["luka", "Lile", "Irakli", "Gio"]
sliced_list =[]
start = 0 
end = len(names)
step = 1
while start < end:
    sliced_list.append(names[start])
    start = start + step
    print(sliced_list)

#3
name = "Luka"
print(name[0:3])


#4
numbers_list = []
start =  5
end = 0
step = -1
while start != 0:
    numbers_list.append(start)
    start = start + step
    print(numbers_list)



#5
names_list = ["Gio", "Luka", "Alex", "Mari"]
sliced_names_list = []
start = len(names_list)
end = 0
step = -1
while start > end:
    sliced_names_list.append(names_list[start])
    start = start + step 
    print(sliced_names_list)