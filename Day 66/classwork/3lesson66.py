def sum_no_duplicates(l):
    numbers = []
    for num in l:
        if l.count(num) == 1:
            numbers.append(num)
    return sum(numbers)

print(sum_no_duplicates([1,1,1,3,4,5]))
            