# create an empty array
ar = []
print(ar)
# append an element
ar.append(1)
print(ar)
# now append a string
ar.append('hello')
print(ar)
# now insert an element
ar.insert(1, 34.32)
print(ar)
# now remove an element
ar.remove(1)
print(ar)
# now pop the element
ar.pop(1)
print(ar)
# now clear all elements
ar.clear()
print(ar)
# now add a range
ar = [i for i in range(1, 10, 1)]
print(ar)
# array with random numbers to use sorted
rand = [3, 4, 2, 1, 5, 6, 4, 7, 9, 8]
print(rand)
print(sorted(rand))
# assign a variable
a, b, c = 2, 3, 5
print("a=", a, "b=", b, "c=", c)
# odd evens using list comprehensions
nums = [str(i) + " is Even" if i%2==0 else str(i) + " is Odd" for i in range(10)]
print(nums)
