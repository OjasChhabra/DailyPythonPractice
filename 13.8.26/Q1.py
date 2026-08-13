# Merge two dictionaries into one.
d1 = {"a": 1, "c": 3}
d2 = {"b": 2, "d": 4}

# Shit Method
# d3 = {}
# for i in d1:
#     d3[i] = d1[i]
# for i in d2:
#     d3[i] = d2[i]
# print(d3)

# Logic Method
for i in d2:
    d1[i] = d2[i]
print(d1)

# Sigma Method
# d1.update(d2)
# print(d1)
# Dayum