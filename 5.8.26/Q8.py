# Checking if the num n is perfect (means whether sum of factors = mun) eg 6 = 1 + 2 + 3
n = int(input("Enter the value of n: "))
sum_of_factors = 0
for i in range(1,n):
    if n % i == 0:
        sum_of_factors += i

if sum_of_factors == n:
    print(f"{n} is a perfect Number")
else:
    print(f"{n} is not a perfect Number")