#bytes example 
print("This is a bytes example")
#createing a bytes object)
b = bytes([104, 101, 108, 108, 111])
print(b)

#accessing elements in bytes object
print(b[0])  # Output: 104
print(b[1])  # Output: 101

#literal through a bytes object
for byte in b:
    print(byte, end ='')  # Output: 104 101 108 108 111
    print() 

    #byteaarray example
print("This is a bytearray example")
#creating a bytearray object
ba = bytearray([104, 101, 108, 108, 111])
print(ba)

#modifying elements in bytearray object
ba[0] = 72  
print(ba)  # Output: bytearray(b'Hello')

#adding elements to bytearray object
ba.append(33)  
print(ba)  # Output: bytearray(b'Hello!')

#converting bytearray to bytes
b_from_ba = bytes(ba)
print(b_from_ba)  # Output: b'Hello!'

#memoryview example
print("This is a memoryview example")
#creating a bytes object
b_mv = bytes([104, 101, 108, 108, 111])

#creating a memoryview object
mv = memoryview(b_mv)
print(mv)

#accessing elements in memoryview object
print(mv[0])  # Output: 104
print(mv[1])  # Output: 101

#silcing memoryview object
mv_slice = mv[1:4]  # Output: <memory at 0x...
print(mv_slice.tobytes())  # Output: <memory at 0x...>

#creating a bytearray from memoryview
ba_from_mv = bytearray([104, 101, 108, 108, 111])
mv_ba = memoryview(ba_from_mv)
print(mv_ba)

#modifying memoryview object
mv_ba[0] = 72
print(mv_ba.tobytes())  # Output: b'Hello'

bytetemp = (bytes([74]))
print(bytetemp)