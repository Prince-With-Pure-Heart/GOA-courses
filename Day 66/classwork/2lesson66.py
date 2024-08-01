def factorial_division(n, d):
    mult = 1
    for i in range(n,-1,-1):
        if i <= d:
            break
        mult *= i
    return mult

print(factorial_division(int(input()), int(input(2
                                                 ))))