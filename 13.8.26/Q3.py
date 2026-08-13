# Count the frequency of each element in a list using a dictionary.
list = ["a","b","a","c","b","a"]
dict = {}
for i in list:
    dict.setdefault(i, 0)
    dict[i] += 1
print(dict)
