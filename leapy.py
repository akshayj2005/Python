
print("Enter the year you want to check for leap year")
y = int(input('year:->  '))

if (y % 4 == 0 and y%100!=0) or(y%400 == 0):
    print("leap year ",y)
else:
    print("not a leap year ",y)

print("THIS CODE IS WRITTE AND EXECUTED BY AKSHAY JAIN 231BCA222")    
