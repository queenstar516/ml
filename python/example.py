x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = ["mango", "orange", "lemon", "coconut", "pineapple"]

for i in x:
    print(i)

for i in range(len(y)):
    print(y[i])

[print(i) for i in x]


z = [i for i in y if i != "lemon"]
print(z)

for i in x:
    if i > 5:
        print(i)
    else:
        print("*")

j = [i if i != "mango" else "orange" for i in y]
print(j)

unsorted = [4, 3, 2, 0, 1, 9, 8, 7]

print(sorted(unsorted))

m = x.copy()
print("Before changing", m)
x[5] = 12
print("After changing:", m)

#------------------------ Tuple --------------------
t = ("apple", "banana", "cherry")
print(t)
myTuple = ("mango",)
print(type(myTuple))

o = t * 2
print(o)
