#iterating over a list of fruits
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


#iterating over a range of numbers
for i in range(5):
    print(i)


#iterating over a string
for char in "hello":
    print(char) 

#iterating over a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}

for key in person:
    print(key, ":", person[key])    


#using else in a for loop
for i in range(3):
    print(i)
else:
    print("Loop completed without break")


#nested for loops
for i in range(2):
    for j in range(3):
        print("i:", i, "j:", j)

#list comprehension 
squares = [x**2 for x in range(10)]
print(squares)

#emuerate for index and value
for index, value in enumerate(fruits):
    print(index, ":", value)
    

