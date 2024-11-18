def invert(lst):
    return [n * -1 for n in lst] if len(lst) > 0 else []


print(invert([1,-2,-3,44,-100]))