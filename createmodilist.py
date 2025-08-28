#python code to create modify a list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
my_list.append(6)
my_list.insert(2,2.5)
my_list.remove(4)
print("List after ", my_list)
print("\n\n\n\n\n")

# slicing  elements of lisT
s = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print("Original list:", s)
print("Elements from index 2 to 5:", s[2:6])
print("Elements from start to index 4:", s[:5])
print("Elements from index 5 to end:", s[5:])
print("Last three elements:", s[-3:])
print("\n\n\n\n\n")

#list comprehension
squares = [x**2 for x in range(1, 11)]
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]

print("Squares of numbers from 1 to 10:", squares)
print("Squares of even numbers from 1 to 10:", even_squares)
print("\n\n\n\n\n")

#create and access a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Elements from index 1 to 3:", my_tuple[1:4])
print("\n\n\n\n\n")

#create and access a nested tuple
nested_tuple = (1, (2, 3), (4, 5, 6), 7)
print("Original nested tuple:", nested_tuple)
print("First element:", nested_tuple[0])
print("Second element (which is a tuple):", nested_tuple[1])    
print("Element 3 of the second element:", nested_tuple[1][2])
print("Elements from index 1 to 2 of the nested tuple:", nested_tuple[1:3])
print("\n\n\n\n\n")