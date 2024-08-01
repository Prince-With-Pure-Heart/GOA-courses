def find_smallest_int(arr):
    # min ფუნქციით ჩვენ დავაბრუნეთ სიის მინიმალური ინდექსი
    return min(arr)
        

print(find_smallest_int(arr = [1,2,3,-1221343, -122312 * 4]))




def to_jaden_case(string):
    if len(string) == 0:
        return string

    name = string.split()
    for i in range(len(name)):
        name[i] = name[i].capitalize()

    return ' '.join(name)


print(to_jaden_case(input("Pelase enter your word:    ")))



def end(text, ending):
    if text.endswith(ending):
      return  True
    else:
        return False

print(end("jeijei", "world"))


 