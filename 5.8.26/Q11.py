# To check if a num is palindrone or not
word = input("Enter the word you want to check: ").lower()
rev = ""

for i in range(len(word),0,-1):
    rev += word[i-1]

if rev == word:
    print(f"{word} is a Palindrone")
else:
    print(f"{word} is not a Palindrone")