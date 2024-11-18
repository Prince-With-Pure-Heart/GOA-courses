def merge_strings(first, second):
    if first == second:
        return first
    res = ""
    index = None
    for i in range(1,len(first) + 1):
        if first[-i:] == second[:i]:
            index = i
    return first + second[index:]

print(merge_strings(input(), input()))