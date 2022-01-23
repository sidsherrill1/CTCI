"""
Problem statement:
Create a dict from one or more lists.
"""

# //----------------------------------------------------------------------------------//
# //
# //


# if the list has all unique members:
l = ["a", "b", "c", "d"]
d = {x: 1 for x in l}
print(d)

# dict comprehension
l = ["a", 1, "b", 2, "c", 3, "d", 4]
d = {l[i]: l[i + 1] for i in range(0, len(l) - 1, 2)}
print(d)

k = ["a", "b", "c", "d"]
v = [1, 2, 3, 4]
d = {k: v for (k, v) in zip(k, v)}
print(d)

# otherwise, if you're trying to make a dict of counts:
l = ["a", "b", "c", "c", "d"]
d = {}
for x in l:
    if x in d:
        d[x] += 1
    elif x not in d:
        d[x] = 1
print(d)
