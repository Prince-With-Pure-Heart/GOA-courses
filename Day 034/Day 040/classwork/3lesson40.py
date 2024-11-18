def descending_order(num):
    result = []
    new_str = ""
    for i in  str(num):
        result.append(int(i))
    result.sort(reverse = True)
    for number in result:
        new_str += str(number)
    return int(new_str)
    

print(descending_order(31))