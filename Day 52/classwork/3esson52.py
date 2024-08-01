def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    result = []
    for num in range(a,b + 1):
        sum = 0
        num_str = str(num)
        for i in range(len(num_str)):
            sum += int(num_str[i]) ** (i + 1)
        if sum == num:
            result.append(num)
    return result


print(sum_dig_pow(int(input()), int(input())))