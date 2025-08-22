try:
   number = int(input("enter a number: "))
   result = 10/number
except ZeroDivisionError:
    print("error: cannot divide by zero.")
except ValueError:
    print("error: invalid input. please enter a valid number.")
print("this program is written and excecuted by MEHAK BHUTANI with ERP 0231BCA063")
