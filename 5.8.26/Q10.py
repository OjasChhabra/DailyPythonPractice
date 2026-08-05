# Reverse a string

word = (input("Enter the text you want to Reverse: "))
# print(word[::-1])
reverse = ""

for i in range(len(word),0,-1):
    reverse += word[i-1]
print(reverse)