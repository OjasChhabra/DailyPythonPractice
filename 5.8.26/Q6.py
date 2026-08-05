# Sum of odd and even num seperatly upto n

n = int(input("Enter the value of n: "))
odd = 0
even = 0
for i in range(1, n+1):
    if i % 2 == 0:
        even += i
    else:
        odd +=i

print(f"Sum of even num are: {even}\nSum of odd num are: {odd}")