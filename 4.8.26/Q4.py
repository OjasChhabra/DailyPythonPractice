# to check if triangle is valid or not
side1 = float(input("Enter side 1:"))
side2 = float(input("Enter side 2:"))
side3 = float(input("Enter side 3:"))

list = [side1, side2, side3]
biggest_side = max(list)
list.remove(biggest_side)

if biggest_side < list[0] + list[1]:
    print("This is a valid config for Triangle")
else:
    print("This is not a Valid config for Triangle")