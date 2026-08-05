# Checking if a num n is palindrone or not
n = int(input("Enter the value of n: "))
original = n
rev = 0
while n != 0:
    rev = (rev * 10) + (n % 10)
    n //= 10
if rev == original:
    print(f"{original} is a Palindrone")
else:
    print(f"{original} is not a Palindrone") 
