# Checking if the list is sorted or not again
list = []
while True:
    n = input("Enter the value or 'STOP' to stop entering: ")
    if n != "stop":
        try:
            a = int(n)
            list.append(a)
        except ValueError:
            print("Enter a valid input!! 😤")
    else:
        break
copy1 = list
copy2 = list
copy1.sort()
copy2.sort(reverse=True)
if list == copy1:
    print(f"List: {list} is sorted in ascending order!! 🥳")
elif list == copy2:
    print(f"List: {list} is sorted in decending order!! 🥳")   
else:
    print(f"List: {list} is not sorted!! 😭")

# This is the better version of earlier program that checks the sorting