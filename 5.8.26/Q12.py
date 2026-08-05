# To check the numbers of character, numbers and symbols in a string
word = "P@#yn26at^&i5ve"
char = 0
special_char = 0
digit = 0

for i in word:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        char += 1
    else:
        special_char += 1
print(f"Char: {char}, Special Char: {special_char}, Digits: {digit}")
