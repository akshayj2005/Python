import numpy as np
a = np.array([[1, 2],[3,4]])
b = np.array([[5,6],[7,8]])
c = np.dot(a, b)
print(c)


# A= {1,'two', 3.0,3,27.5,'four', 5}
# B={27.5,10}
# print(A|B)


A=np.array([range(i,i+4) for i in [1,3,5]])
print(A)






Product = ["pencil", "eraser", "sharpener", "ruler"]
Price = [10, 5, 15, 20]
Brand = ["A", "B", "C", "D"]
Stationary = [Product, Price, Brand]
Stationary[0].insert(0, "Notebook")