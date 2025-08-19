a = 10
b = 5

#first way
temp = a
a = b
b = temp
print(a)
print(b)

#second way
a = a+b
b = a-b
a = a-b
print(a)
print(b)

#third way
a,b = b,a
print(a)
print(b)
