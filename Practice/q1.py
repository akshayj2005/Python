"""List of Python Practical Questions :-

# Chapter - 1 (Introduction To Python) :-

1. Write a program to print hello world."""

# print("Hello, World!")
"""
2. Write a program to print your name."""

# name = "Akshay Jain"
# print("My name is", name)
"""
3. Write a program to check the valid identifiers."""

# identifier = "my_variable"
# if identifier.isidentifier():
#     print(f"{identifier} is a valid identifier.")
# else:
#     print(f"{identifier} is not a valid identifier.")


""""

4. Write a program to check the invalid identifiers."""

# invalid_identifier = "1st_variable"
# if invalid_identifier.isidentifier():
#     print(f"{invalid_identifier} is a valid identifier.")
# else:
#     print(f"{invalid_identifier} is not a valid identifier.")
"""
5. Write a program to show single line comment."""
# # This is a single line comment in Python
# print("This line is not a comment.")


"""
6. Write a program to show multiline comment.
"""
# """'''
# This is a multiline comment in Python.
# ouebsvjn iojs bvohi
# """'''
"""

7. Write a program to show doc string comment."""
# def example_function():
#     '''This is a docstring comment for the example_function.'''
#     pass
# print(example_function.__doc__)
"""

8. Write a program to define a simple function."""

# def greet():
#     print("Hello! Welcome to Python programming.")
# greet()



"""
# 9. Write a program to define variables and types of data for integer and float.
"""
# a = 10
# b = 20.5
# print("Data type of a:", type(a))
# print("Integer:", a)
# print("Data type of b:", type(b))
# print("Float:", b)


"""
10. Write a program on datatype, string, boolean, tuples."""

# a = "hello"
# b = True
# c = (1,2,3,4,5,6,7)

# print(f"Data type of a = {type(a)}")
# print(f"Data type of b = {type(b)}")
# print(f"Data type of c = {type(c)}")
"""

11. Write a program on datatype, list, set & dictionary."""

# a = [1,2,3,5,5,6,4,5,5,6,5,15,68,1,15,541,5,84,1,5,8,1,58]
# b = {1,2,51,2,6,1,58,1}
# c = {1:"aksha", 2:"kjsvcib"}

# print(f"Data type of a = {type(a)}")
# print(f"Data type of b = {type(b)}")
# print(f"Data type of c = {type(c)}")


"""

12. Write a program to get a name from user."""

# a = input("Enter your name\n")
# print(f"Your Name = {a}")
"""

13. Write a program on getting a number & add 10."""
# a = (int)(input("Enter any number \n"))
# print(f"Numeber after adding 10 = {a+10}")
"""

# 14. Write a program on getting multiple inputs from user & print.
# """
# a = input("Enter multiple values seperated by comma(,)\n")
# b = a.split(",")

# for i in b:
#     print(i.strip())

"""
15. Write a program to perform basic mathematics operations."""

# a = 5
# b = 10
# print(f"Add = {a+b}")
# print(f"Sub = {a-b}")
# print(f"Div = {a/b}")
# print(f"Mul = {a*b}")
# print(f"Mod = {b%a}")

"""
16. Write a program to perform math operations using math module."""

# import math as m

# a= 5.5
# b = 25

# print(m.pow(a,b))
# print(m.sqrt(b))
# print(m.ceil(a))
# print(m.floor(a))
# print(m.factorial(b))
# print(round(m.pi,4))
"""
17. Write a program to perform a binary type data type."""
# a = b"hello"
# print(a)
# for i in range(len(a)):
#     print(a[i])

"""
18. Write a program to take a list of numbers from user, calculate sum and sort the list."""
# a = (input("Enter elements of list seperated by (,)\n"))
# b = [(int)(i) for i in a.split(",")]
# #1,5,6,8,5,96,5
# #[1,5,6,8,5,96,5]
# c = sum(i for i in b)
# d = sorted(b)

# print(b)
# print(c)
# print(d)
"""
Chapter - 2 (Statements And Control Structures) :-

19. Write a program to swap two variables without using a 3rd variable or any control statement."""

# a = 5
# b = 6
# c = 8

# print(a)
# print(b)
# print(c)
# print()
# a= a+b
# b= a-b
# a = a-b

# a,b = b,a
# a = a+b+c  
# b = a-(b+c)
# c = a-(b+c)
# a = a-(b+c)


# print(a)
# print(b)
# print(c)
# print()

"""
20. Write a program to check if a number is positive, negative or zero."""
# a= -5
# if(a>0):
#     print(f"{a} is positive")
# elif(a<0):
#     print(f"{a} is negative")
# else:
#     print(f"{a} is zero")
    
    
"""
21. Write a program to check whether a number is odd or even."""
# a = 5
# if(a%2==0):
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")


"""
22. Write a program to check whether the year is leap year or not."""
# a = 1900

# if(a%4==0 and a%100!=0) or ( a%400==0):
#     print(f"{a} is leap")
# else:
#     print(f"{a} is not leap")

"""
23. Write a program to print the last digit of given integer number."""
# a= 1548658
# b = a%10
# print(b)
"""
24. Write a program to calculate the percentage of a student through 5 subjects (take marks as input from user)."""
# a = (input("Enter Marks of 5 subjects seperated by (,)\n"))
# b = [(int)(i) for i in a.split(",")]
# c = sum(b)
# d = round((c/(len(b)*100))*100,2)
# print(f"Percentage of marks = {d}%")


"""
25. Write a program to grade the student according to the percentage given below :-
If above 90% then A+
If between 80% and 90% then A 
If between 70% and 80% then B
If between 60% and 70% then C
Else D"""
# a = 95
# if(a>90):
#     print("A+")
# elif(a>80 and a<=90):
#     print("A")
# elif(a>70 and a<=80):
#     print("B")
# elif(a>60 and a<=70):
#     print("C")
# else:
#     print("D")

"""

26. Write a program to get user input and save report to a file."""
# name = input("Enter the Name\n")
# age = input("Enter age\n")

# with open("report.txt", "w") as file:
#     file.write(f"==========Report file==========\n\t\tName = {name}\n\t\tAge = {age}\n===============================")
#     print("report saved")
"""
27. Write a program to check if a single character is vowel or not."""

# a = "x"
# b = ["a", "e", "i", "o", "u"]
# if a in b:
#     print("Vowel found")
# else:
#     print("Vowel Not Found")
"""
28. Write a program to check if a number is divisible by 2 and 3."""
# a = 6
# if (a%3 == 0 and a%2 == 0):
#     print("Divisible by both 2 and 3")
# else:
#     print("bhak")

"""
29. Write a program to check the largest of the three numbers."""
# a= 5
# b = 9
# c = 7

# print(max(a,b,c))
"""

30. Write a program to check login and password."""
# a = {"akshay":"Akshay123", "yuvi":"yuvi123"}
# b = input("Enter your username\n")
# c = input("Enter your password\n")

# if b in a: #username i.e key
#     if a[b] == c: #password i.e value 
#         print("Correct ✅")
#     else:
#         print("Wroung ❌")
# else:
#     print("Wroung ❌")


"""
31. Write a program to determine season based on month."""
# a = 5

# if a in (12,1,2):
#     print("Winter")
# elif a in (3,4,5):
#     print("Spring")
# elif a in (6,7,8):
#     print("Summer")
# elif a in (9,10,11):
#     print("Autumn")
# else:
#     print("Range ma aa 1-12")
"""
32. Write a program to find the factorial of a number."""
# a = 5 
# b = 1
# for i in range(a,0,-1):
#     b *= i
# print(b)

"""

33. Write a program to print the table from 2 to 10."""
# a = [i for i in range(2,11)]
# for i in a:
#     print(f"\n\n{i}'s table")
#     for f in range(1,11):
#         print(f"{i} x {f} = {i*f}")

"""
34. Write a program to convert celsius to fahrenheit taking celsius as input."""
##f = (C x 9/5)+32
# a = 42
# b = (a*(9/5))+32
# print(round(b,2))

"""

35. Write a program to check whether the number is prime number or not."""

# a = 19

# if a>1:
#     is_prime = True
#     for i in range(2,a):
#         if a%i == 0:
#             is_prime = False
#             break
#     if(is_prime):
#         print("prime")
#     else:
#         print("not")
# else:
#     print("not")    
"""
36. Write a program to check prime numbers between the given range."""
# b = (int)(input("Enter starting of range"))
# c = (int)(input("Enter ending of range"))
# count = 0
# def prime(a):
#     global count
#     if a>1:
#         is_prime = True
#         for i in range(2,a):
#             if a%i == 0:
#                 is_prime = False
#                 break
#         if(is_prime):
#             print(a) 
#             count += 1
# for i in range(b,c):
#     prime(i)
# print("\n\n",count, " hell ")
"""
37. Write a program to check the ATM pin using the break statement."""
# correct_pin = "1234"

# for i in range(3):  # Allow 3 attempts
#     pin = input("Enter your PIN: ")

#     if pin == correct_pin:
#         print("PIN accepted. Access granted.")
#         break
#     else:
#         print("Incorrect PIN.")
# else:
#     print("Limit reached come after some time")
"""

38. Write a program to ask the user to input a number (1 - 7) and display the corresponding day.
"""
# a = (int)(input("Enter the number of corresponding day (1-7):-    "))
# match(a):
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tues")
#     case 4:
#         print("Wed")
#     case 5:
#         print("Thur")
#     case 6:
#         print("Fri")
#     case 7:
#         print("Sat")
#     case _:
#         print("Enter in range")
    
"""

39. Write a program to check if a number is armstrong or not."""
# a = (input ("enter a numeber"))
# s = sum(int(i)**(len(a)) for i in str(a))
# if (int)(a) == s:
#     print("Armstrong")
# else:
#     print("not")

"""
40. Write a program to print armstrong numbers from 1 to 1000.
"""
# count = 0
# def arm(a):
#     global count
#     s = sum((int)(i)**(len(a)) for i in (str)(a) )
#     if ((int)(a) == s):
#         print(a)
#         count += 1

# for i in range(1,1001):
#     arm((str)(i))
# print("\n\n",count)
"""

41. Write a program to find the sum of natural numbers."""
# s = 0
# for i in range(1,101):
#     s += i
# print(s)
# #sum = total no of natural no (total no of natural no+1)//2

# n = 100
# s = n * (n + 1) // 2
# print("Sum is:", s)

"""
42. Write a program to print the Fibonacci sequence."""
# def fib(a):
#     if a == 0:
#         return 0
#     elif a== 1:
#         return 1
#     else:
#         return (fib(a-1) + fib(a-2))

# for i in range(0, 10):
#     print(fib(i), "  ") 

"""
Chapter - 3 (List, Ranges & Tuples & Dictionaries In Python) :-

43. Write a program to perform different operations on strings.
"""
# s = "hello"
# b = s[0]
# c = s[:3]
# d = s[0]+s[:3]
# e = s*3
# print(s)
# print(b)
# print(c)
# print(d)
# print(e)

# for i in s:
#     print(i)
"""

44. Write a program to perform different operations on the list."""
# a = [1,2,5,4,6,61,5]
# b = a[0]
# c = a[:5]
# d = [a[0]]+a[:5]
# e = a.append(10)
# f = a.pop()
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# a.insert(1,25)
# print(a)

"""

45. Write a program to determine whether the given string is a palindrome or not using slicing.
"""
# s = (input("enter some thing")).lower()
# a = 0
# b = (len(s) - 1)
# pal = True
# while a<b:
#     if s[a] != s[b]:
#         pal = False
#         break
#     a+= 1
#     b-=1

# if(pal):
#     print("Palindrome")
# else:
#     print("no")
"""

46. Write a program to demonstrate string traversing using the for loop."""
# s = "hello"
# for i in s:
#     print(i)
"""

47. Write a program to print the characters which are common in 2 strings.
"""
# s= "helsdf"
# a = "oseinonwj"
# aa = set(a)
# ss = set(s)
# d = set(aa & ss)
# print(d)
"""
48. Write a program to calculate the length of a string without using the built-in len() function.
"""
# s = "hello"
# count = 0
# for i in s:
#     count+=1
# print(count)

"""

49. Write a program to count the occurrence of the user - entered words in a sentence."""
# s = "python is fun and I used to practice python a lot".lower()
# d = "python".lower()

# w = s.split()
# wo = w.count(d)
# print(wo)

"""

50. Write a program to perform different operations on tuples."""

# t = (10, 20, 30, 40, 20)
# print(t[1])
# print(len(t))
# print(t.count(20))
# print(t.index(30))
# print(t + (50,))

"""

51. Write a program to perform different operations on dictionaries."""

# d = {'x': 5, 'y': 10}
# d['z'] = 15
# d['x'] = 20
# print(d.get('y'))
# del d['y']
# print(d)


"""
52. Write a program to use len(), del, remove (), and range() on list/tuple."""
# l = [1,2,3,5,4]
# print(l)
# a = len(l)
# del l[0]
# l.remove(3)
# ll = list(range(1,10))
# print(a)
# print(l)
# print(ll)

"""
53. Write a program to demonstrate usage of map() and filter on a list."""
# l = [1,2,3,5,4]
# m = map(lambda x:x*2, l)
# print(list(m))

# f = filter(lambda x:x%2==0,l)
# print(list(f))

"""
54. Write a program to perform different range functions."""
# for i in range(1,10,2):
#     print(i)
# print()
# for i in range(10):
#     print(i)
# print()

# for i in range(1,10):
#     print(i)
# print()

# for i in range(10,0,-1):
#     print(i)
"""
55. Write a program to perform set operations."""
# a = {1,2,3}
# b = {3,4,5}
# a.add(100)
# a.remove(2)
# a.pop()

# print("Set A:", a)
# print("Union:", a | b)
# print("Intersection:", a & b)
# print("Difference:", a - b)
# print("Difference:", b - a)
# print("Symmetric Difference: ", a^b)
# print("length:", len(a))
# print("length:", len(b))

"""
56. Write a program to use yield in a custom iterator."""

# def my_iterator(n):
#     for i in range(n):
#         yield i

# for value in my_iterator(5):
#     print(value)

"""
57. Write a program to use a generator with yield."""
# def my_generator():
#     yield "Hello"
#     yield "World"
#     yield "!"

# for word in my_generator():
#     print(word)

"""
58. Write a program to use list comprehension with condition, to use set comprehension.
"""
# l = [x**2 for x in range(1,6) if x%2==0]
# s = {x*x for x in range(1,6)}
# print(l)
# print(s)

"""
59. Write a program to create and use different generations in python.
"""
# # Generator function
# def gen_func(n):
#     for i in range(n):
#         yield i * 2

# Generator expression
# gen_expr = (x * 3 for x in range(5))

# g1 = gen_func(5)
# g2 = gen_expr

# print(next(g1))  # 0
# print(next(g1))  # 2
# print(next(g2))  # 0
# print(next(g2))  # 3

# for val in g1:
#     print(val)

# for val in g2:
#     print(val)

"""
60. Write a program to create iterators.
"""
# class h:
#     def __init__(self,n):
#         self.n = n
#         self.c = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if (self.n <= self.c):
#             raise StopIteration
#         else:
#                 self.c += 1
#                 return self.c 

# db = h(5)
# for i in db:
#     print(i)

"""
61. Write a program to count the total number of vowels, consonants and blanks in a string.
"""
# s = "iisdn ijsai cjs jijsn i nvsc bvknshkvohi kfbnc jilkvilkcn jikm hnijdkvnjiknvkhn pojclnjl".lower()

# v = "aeiou"
# c = "bcdfghjklmnpqrstvwxyz"
# vc = 0
# cc = 0
# bc = 0
# for cd in s:
#     if cd in v:
#         vc+=1
#     elif cd in c:
#         cc+=1
#     elif cd == ' ':
#         bc+=1

# print("vovel  = ", vc)
# print("blank  =  ",bc)
# print("consonent = ",cc)


"""
Chapter - 4 (Functions, Modules, Packages and DebuggingFunctions) :-

62. Write a program for the def function definition with arguments and without arguments.
"""
# def fnwa(a):
#     for i in range(a):
#         print(i)

# def greet():
#     print("Good Morning")

# fnwa(5)
# greet()

"""
63. Write a program in python to find the lcm of 2 numbers.
"""
# a = 5
# b = 22
# def lcm(aa, bb):
    
#     for i in range(max(aa,bb),(aa*bb)+1):
#         if (i%aa == 0 and i%bb==0):
#             print(i)
#             break
# lcm(a,b)
"""
64. Write a program to find the lcm of multiple numbers.
"""
# def lcm(aa, bb):
    
#     for i in range(max(aa,bb),(aa*bb)+1):
#         if (i%aa == 0 and i%bb==0):
#             return i

# def mullcm(num):
#     first = num[0]
#     for i in num[1:]:
#         first = lcm(first,i)
#     return first

# nu  = [5,65,15,20]
# print(mullcm(nu))
"""
65. Write a program for function definition with no return argument.
"""
# a = 5
# b = 22
# def lcm(aa, bb):
    
#     for i in range(max(aa,bb),(aa*bb)+1):
#         if (i%aa == 0 and i%bb==0):
#             print(i)
#             break
# lcm(a,b)
"""
66. Write a program for usage of function returning values.
"""
# def num(a,b):
#     return a+b

# print(num(5,6))
"""
67. Write a program for real life examples to calculate the bank interest.
"""
# def si(p,r,t):
#     return ((p*r*t)/100)

# print(f"Interest = {si(10000,5,2)}")
# print(f"Total = {10000+si(10000,5,2)}")
"""
68. Write a program where you use both print and return in the same program (percentage calculation).
"""
# def per(num):
#     total = sum(num)
#     perce = (total/(len(num)*100)*100)
#     print("Percetnage got = ", perce,"%")
#     return perce
# number = [25,95,85,68,45]

# if (per(number)>60):
#     print("pass")
# else:
#     print("fail")
"""
69. Write a program to find the hcf of two numbers.
"""
# def find_hcf(a, b):
#     hcf = 1
#     for i in range(1, min(a, b)+1):
#         if a % i == 0 and b % i == 0:
#             hcf = i
#     return hcf

# # Example usage:
# a = 54
# b = 24
# print(f"HCF of {a} and {b} is", find_hcf(a, b))

"""
70. Write a program to convert decimal numbers to binary, octal and hexadecimal.
"""
# num = float(input("Enter a decimal number: "))

# print("Binary     :", bin(num))
# print("Octal      :", oct(num))
# print("Hexadecimal:", hex(num))

"""
71. Write a program to find the ASCII value of a character.
"""
# s = "F"
# a = (ord)(s)
# print(a)
"""
72. Write a program to print a fibonacci sequence using a recursive function.
"""
# def fib(a):
#     if a == 0:
#         return 0
#     elif a== 1:
#         return 1 
#     else:
#         return (fib(a-1)+fib(a-2))
# b = 5
# for i in range(0,b):
#     print(fib(i), end = "  ")
"""
73. Write a program to display calendar.
"""
# import calendar

# year = int(input("Enter year: "))
# month = int(input("Enter month (1-12): "))

# print("\nHere is the calendar:")
# print(calendar.month(year, month))

"""
74. Write a program to print the factorial of numbers using recursive functions.
"""
# def fac(a):
#     if a == 1 or a == 0:
#         return 1
#     else:
#         return a * fac(a - 1)

# print(fac(5))

"""
75. Write a program to demonstrate positional parameters.
"""
# def add(a,b):
#     return a+b
# print(add(5,6))

"""
76. Write a program to demonstrate keyword parameters.
"""
# def greet(h, j):
#     print(f"Hello {h}\nyou are now {j}")
# greet(j=20,h="Akshay")
"""
77. Write a program to demonstrate variable length parameters.
"""
# def add(*args):
#     print(sum(*args))
# num = [1,5,26,5,9,5,6,4,6,8,4]
# add(num)

# def details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"key = {key}, value = {value}")

# dic = {'1':"dhgh", '2':"dhfdhgfh"}
# details(**dic)
"""
78. Write a program to create a login system into a role-based access control system using decorators.
"""
# user = {"Akshay":"Akshay123", "yuvi":"yuvi123"}
# admin = {"Admin":"Admin123"}

# role = ""
# def login(username, password, role_d):
#     global role
#     if (username in role_d and role_d[username] == password):
#         role = role_d
#         print("success")
#     else:
#         print("cant login")

# def hel(roles):
#     def decorator(func):
#         def wrapper():
#             if (roles==role):
#                 func()
#             else:
#                 print("no access")
#         return wrapper
#     return decorator
 
# @hel(admin)
# def admin_g():
#      print("welcome admin")
# @hel(user)
# def user_g():
#      print("welcome user")     
# login("Admin","Admin12", admin)
# admin_g()
# login("Akshay", "Akshay123", user)
# user_g()
"""
Chapter - 5 (Python Object Oriented) :-

79. Write a program to create a using the class keyword, and an object is created by calling the class.
"""
# class hell():
#     def __init__(self, name):
#         self.name = name
    
#     def greet(self):
#         print(f"Hello brother {self.name}")

# h = hell("Akshay")
# h.greet()

"""
80. Write a program to demonstrate the difference between abstraction and encapsulation.
"""
# from abc import ABC, abstractmethod
# class car(ABC):
#     @abstractmethod
#     def speed(self):
#         pass
# class swift(car):
#     def speed(self):
#         print("255kmph")

# a = swift()
# a.speed()

# class bank():
#     def __init__(self):
#         self.__balance = 0
    
#     def deposit(self, amount):
#         if(amount>0):
#             self.__balance += amount
#             print("Deposit done")
#         else:
#             print("cant deposit")
    
#     def bankbalance(self):
#         print(self.__balance)

# b = bank()
# b.deposit(2000)
# b.bankbalance()
        
"""
81. Write a program to demonstrate encapsulation.
"""

# class bank():
#     def __init__(self):
#         self.__balance = 0
    
#     def deposit(self, amount):
#         if(amount>0):
#             self.__balance += amount
#             print("Deposit done")
#         else:
#             print("cant deposit")
    
#     def bankbalance(self):
#         print(self.__balance)

# b = bank()
# b.deposit(2000)
# b.bankbalance()
        
"""
82. Write a program to demonstrate inheritance.
"""
# class car():
#     def speed(self):
#         print("40")

# class swift(car):
#     def speed(self):
#         print("255")

# a = car()
# b = swift()
# a.speed()
# b.speed()


"""
83. Write a program to demonstrate polymorphism.
"""
# class Bird:
#     def speak(self):
#         print("Some generic bird sound")

# class Sparrow(Bird):
#     def speak(self):
#         print("Chirp Chirp")

# class Parrot(Bird):
#     def speak(self):
#         print("Squawk")

# def make_bird_speak(bird):
#     bird.speak()

# b1 = Sparrow()
# b2 = Parrot()
# b3 = Bird()

# make_bird_speak(b1)  
# make_bird_speak(b2)  
# make_bird_speak(b3)  

"""
84. Write a program to build a real world OOP case study (Library Management System)."""
# class book():
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.issue= False
    
#     def __str__(self):
#         if (self.issue == False):
#             self.status = "Available"
#         else:
#             self.status = "Issued"
#         return f"{self.title} by {self.author} is {self.status}"
    

# class library():
#     def __init__(self):
#         self.books = []
    
#     def addbook(self, title, author):
#         b = book(title, author)
#         self.books.append(b)
#         print("added")
    
#     def display(self):
#         if not self.books:
#             print("no books")
#         else:
#             for b in self.books:
#                 print(b)


#     def issuebk(self, title):
#         for b in self.books:
#             if b.title == title:
#                 if b.issue:
#                     print("already issued")
#                 else:
#                     b.issue = True
#                     print("issued to you")
    
#     def retbook(self, title):
#         for b in self.books:
#             if b.title == title:
#                 if b.issue:
#                     b.issue = False
#                     print("book returned")
#                 else:
#                     print("havent issued till now ")

# lib = library()
# lib.addbook("Harry Potter", "J.K. Rowling")
# lib.addbook("The Alchemist", "Paulo Coelho")

# lib.display()
# lib.issuebk("Harry Potter")
# lib.display()
# lib.retbook("Harry Potter")
# lib.display()

"""
85. write a code input number and sum them and find prime digits in them and unique primes sum will be sum"""
# a = (input("Enter any number"))
# b = sum((int)(i) for i in a)
# number = {'1','2','3','5','7'}
# c = set(str(b)) & number

# d = sum((int)(i) for i in (c))
# print(f"Discount = {d}")

"""
86. write a custom exception code"""
# class InvalidAgeError(Exception):
#     def __init__(self, age, message="Age must be between 0 and 120"):
#         self.age = age
#         self.message = message
#         super().__init__(f"{message}. Got: {age}")

# # Usage
# def set_age(age):
#     if age < 0 or age > 120:
#         raise InvalidAgeError(age)
#     print(f"Age set to: {age}")

# try:
#     set_age(130)
# except InvalidAgeError as e:
#     print(e)
# finally:
#     print("rest code")