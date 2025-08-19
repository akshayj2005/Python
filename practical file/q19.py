y=1
i = 1
for y in range(1,2025): 
    if (y % 4 == 0 and y%100!=0) or(y%400 == 0):
        print(i,")  leap year ",y)
        i=i+1
    # else:
    #     print("not a leap year ",y)

print("total number of leap years between are ",i-1)
