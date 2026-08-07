# Make a list sorted
number = []
while True:
    n = input("Enter the value of n or type 'STOP' to stop: ").lower()
    if n != "stop":
        number.append(int(n))
    else:
        break
sorted = []
while len(number) != 0:
    n = number[0]
    for i in number:
        if i > n:
            n = i
    number.remove(n)
    sorted.insert(0, n)

print(sorted)
