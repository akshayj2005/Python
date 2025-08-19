a = 7
b = 5
c = 2

#first way
temp = a
a = b
b = c
c = temp
print(a)
print(b)
print(c)

#second way
a = a+b
b = a-b
a = a-b
c = a+c
c = a-c
a = a-c
print(a)
print(b)
print(c)

#third way
a,b,c = c,a,b
print(a)
print(b)
print(c)
