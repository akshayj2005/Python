# 1. math - mathematical functions
import math
print(math.sqrt(25))  # Output: 5.0

# 2. random - generate random numbers
import random
print(random.randint(1, 10))  # Random int between 1 and 10

# 3. datetime - date and time operations
import datetime
print(datetime.datetime.now())  # Current date and time

# 4. os - interacting with operating system
import os
print(os.name)  # Name of the OS (e.g., 'posix', 'nt')

# 5. sys - system-specific parameters and functions
import sys
print(sys.version)  # Python version

# 6. json - JSON encoding and decoding
import json
data = {'name': 'Alice', 'age': 25}
json_str = json.dumps(data)
print(json_str)  # '{"name": "Alice", "age": 25}'
