# Find the greatest element and print its index.
number = []
while True:
    n = input("Enter the value of n or type 'STOP' to stop: ").lower()
    if n != "stop":
        number.append(int(n))
    else:
        break
highest_num = number[0]
index = 0
for i in number:
    if i > highest_num:
        highest_num = i
        index = number.index(i)
print(f"Highest Num is {highest_num} at index {index}")