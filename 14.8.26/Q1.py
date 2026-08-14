# Combine two dicts, adding values for common keys.
d1 = {"a":5, "b":3}
d2 = {"b":4, "c":2}
for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]
print(d1)