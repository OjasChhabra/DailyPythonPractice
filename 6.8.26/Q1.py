# Print positive and negative element sepratly from a list
number = []
while True:
    n = int(input("Enter the value of n or type '0' to stop: "))
    if n != 0:
        number.append(n)
    else:
        break
positive = []
negative = []
for i in number:
    if i >= 0:
        positive.append(i)
    elif i < 0:
        negative.append(i)
print(f"Postive: {positive}, Negative: {negative}")
 