def get_count(sentence):
    count = 0
    vowels= "aeiou"
    for char in sentence:
        if char in vowels:
            count += 1
    return count
  
print(get_count(input()))
# or

def get_count(sentence):
    return sum(vowel in 'aeiou' for vowel in sentence)



print(get_count(input()))