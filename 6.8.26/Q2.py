# Find the mean of the list
number = []
while True:
    n = input("Enter the value or 'STOP' to stop entering: ")
    if n != "stop":
        try:
            a = int(n)
            number.append(a)
        except ValueError:
            print("Enter a valid input!! 😤")
    else:
        break
total_sum = 0
for i in number:
    total_sum += i

mean = total_sum/len(number)
print(f"Mean: {mean}")