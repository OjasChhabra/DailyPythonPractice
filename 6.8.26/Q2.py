# Find the mean of the list
number = [5, 10 , 15, 20, 25]
total_sum = 0
for i in number:
    total_sum += i

mean = total_sum/len(number)
print(f"Mean: {mean}")