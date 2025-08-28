#create and modify dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
my_dict['age'] = 31  # Update age
my_dict['profession'] = 'Engineer'  # Add new key-value pair
print(my_dict)

#accessing values
print("Name:", my_dict['name'])
print("Age:", my_dict.get('age'))
# Removing a key-value pair
del my_dict['city']
print("Updated Dictionary:", my_dict)

