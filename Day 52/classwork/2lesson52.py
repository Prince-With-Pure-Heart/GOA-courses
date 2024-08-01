def sort_array(source_array): 
    odd_list = []
    for i in source_array:
        if i % 2 != 0:
            odd_list.append(i)
    odd_list.sort()

    index = 0
    result = []
    for x in source_array:
        if x % 2 != 0:
            result.append(odd_list[index])
            index += 1
        else:
            result.append(x)
    return result

print(sort_array([7,1,9,4,10,7,3,2]))