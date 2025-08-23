count = 0
while count<10:
    count+=1
    if count%2==0:  #check if the count is even
        continue #skip the rest of the loop body for even counts
    print(count) #print only odd counts
