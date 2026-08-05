# Print a num n in reverse (not using string btw)
n = int(input("Enter the value of n: "))
rev = 0
while n != 0:
    rev = (rev * 10) + (n % 10)
    n //= 10
print(rev)