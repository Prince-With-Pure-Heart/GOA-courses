def first_non_repeating_letter(s):
    s_low = s.lower()
    for char in s:
        if s_low.count(char.lower()) == 1:
            return char
    return ""


print(first_non_repeating_letter(input()))