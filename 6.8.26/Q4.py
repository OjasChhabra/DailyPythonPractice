# Find the second gretest number from a list
number = []
while True:
    n = input("Enter the value of n or type 'STOP' to stop: ").lower()
    if n != "stop":
        number.append(int(n))
    else:
        break
highest_num = number[0]
index1 = 0
second_highest = number[0]
index2 = 0
for i in number:
    if i > highest_num:
        second_highest = highest_num
        index2 = index1
        highest_num = i
        index1 = number.index(i)
print(f"Highest Num is {highest_num} at index {index1}")
print(f"Second Num is {second_highest} at index {index2}")
