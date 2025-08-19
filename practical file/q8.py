#Bytes Example
print("Bytes Example")
#creating a bytes object
b=bytes([65,66,67,68])
print(b) #output : b'ABCD'

#accesing elements in a byte object
print(b[0]) #output:65
print(b[1]) #output:66

#iterating through a bytes object
for byte in b:
    print(byte, end=' ') #output: 65,66,67,68
print("\n")

#ByteArray Example
print("ByteArray Example")
#creating a bytearray object
ba= bytearray([65,66,67,68])
print(ba) #output : bytearray(b'ABCD')

#modifying elements in a bytearray
ba[0] = 97 #changing 'A'(65) to 'a' (97)
print(ba) #output: bytearray(b'aBCD')

#adding elements to a bytearray
ba.append(69) #adding'E'(69)
print(ba) #output: bytearray(b'aBCDE')

#converting bytearray to bytes
b_converted= bytes(ba)
print(b_converted) #output: b'aBCDE'
print("\n")

#memoryview example
print("MemoryView Example:")
#creating a bytes object
b_mv= bytes([65,66,67,68,69])

#creating a memoryview object
mv = memoryview(b_mv)
print (mv) #output : <memory at 0x000002373DCEFD00>

#accessing elements through memoryview
print(mv[0]) #output : 65

#slicing memoryview
mv_slice = mv[1:4]
print(mv_slice.tobytes()) #output: b'BCD'

#creating a bytearray and a memoryview
ba_mv= bytearray([65,66,67,68,69])
mv_ba =  memoryview(ba_mv)
print(mv_ba)

#modifying the original bytearray through memoryview
mv_ba[0] = 97 #changing 'A' (65) to 'a' (97)
print(ba_mv) #output : bytearray(b'aBCDE')

byte_temp=65
print(byte_temp)

byte_temp="A"
print(byte_temp)

byte_temp=65
print(bytes(byte_temp))

byte_temp="A"
print(bytes(byte_temp))