# a = [1, 2, 3]
# print(id(a[:2]))


x = 100
y = x
print(id(x))
print(id(y))

y = y + 1

print(x)
print(y)
print(id(x))
print(id(y))
