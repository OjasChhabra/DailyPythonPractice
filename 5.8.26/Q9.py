# Checking if a num is prime or not
n = int(input("Enter the value of n: "))
factors = 0
for i in range(1,n+1):
    if n % i == 0:
        factors += 1
if factors <= 2:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")