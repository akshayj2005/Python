#create and modify dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
my_dict['age'] = 31  # Update age
my_dict['profession'] = 'Engineer'  # Add new key-value pair
print(my_dict)
print("\n\n\n\n\n")

#accessing values
print("Name:", my_dict['name'])
print("Age:", my_dict.get('age'))
# Removing a key-value pair
del my_dict['city']
print("Updated Dictionary:", my_dict)
print("\n\n\n\n\n")

#to demonstrate build in iterators
my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print("\n\n\n\n\n")


#use iterator in for loop
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)
for value in my_iter:
    print(value)
print("\n\n\n\n\n")

#custom iterator class
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1