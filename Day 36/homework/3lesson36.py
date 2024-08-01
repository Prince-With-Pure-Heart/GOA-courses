def manual_count(lst,word):
    count = 0
    for element in lst:
        if element == word:
            count += 1
    return count

print(manual_count([input(), input(), input(), input()], input()))