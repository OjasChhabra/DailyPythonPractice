list = []
n = int(input('Enter the value of n: '))
for i in range(1,n+1):
    row = []
    for j in range(n):
        row.append(0)
    row.pop(i-1)
    row.insert(i-1, 1)
    list.append(row)
print(list)