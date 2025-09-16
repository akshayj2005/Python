import math
def is_prime(n):
    if n < 1:
        return False
    elif n == 1:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        return False
    return True

a= int(input("Enter Your Bill Total ="))
b =0
temp = a
while temp > 0:
    b+=temp%10
    temp= temp // 10
l =[]
temp =b
while temp >0:
    f=  temp % 10
    temp =temp // 10
    if is_prime(f):
        l.append(f)
unique_primes = list(set(l))
discount  = sum(unique_primes)
print(f"Discount = {discount}%")

print("------------------------------------------------------------------")
print("   THIS CODE IS WRITTEN AND EXECUTED BY AKSHAY JAIN 0231BCA222")    
print("------------------------------------------------------------------")
