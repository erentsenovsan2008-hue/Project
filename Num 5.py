values = [3, 1, 3, 2, 1, 5, 2]
unque_values = set(values)
other = {2, 4, 5}
a = unque_values & other
b = unque_values | other
r1 = unque_values - other
r2 = other - unque_values
print(r1, r2)
