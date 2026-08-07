# Check if the list is already sorted. 
number = []
while True:
    n = input("Enter the value of n or type 'STOP' to stop: ").lower()
    if n != "stop":
        number.append(int(n))
    else:
        break

for i in number:
    current_index = number.index(i)
    if current_index != (len(number) - 1):
        if i >= number[current_index + 1]:
            print(f"{number} is not a sorted list")
            break
else:
    print(f"{number} list is sorted")

