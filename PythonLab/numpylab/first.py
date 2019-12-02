import numpy as np

a = np.array([1, 2, 3], dtype='int8')
b = np.array([[1, 2, 3], [4, 5, 6]], dtype='int16')


# get shape
print('#shape')
print(a.shape)
print(b.shape)

# get type
print('#datatype')
print(a.dtype)
print(b.dtype)

# get size
print('#size')
print(a.size)
print(b.size)

# get itemsize
print('#itemsize')
print(a.itemsize)
print(b.itemsize)


# get specific
sales = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]])


print(sales[1, 3])  # speific row & column
print(sales[:, 3])  # all rows and specific column
print(sales[1, :])  # specific row and all columns
print(sales[1:2, 1:3])
