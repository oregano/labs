# tuples
days = ('Sun', 'Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat')
# print(type(days))
# print(days)

# lists
junk = ['this is a string', 'second word', 22, 44, 5.5]
# print(type(junk))
# print(junk)

# dictionary
emp = {"Kaifee Mohammad": "kaifee@microsoft.com",
       "Chris": "chris@microsoft.com"}
# print(type(emp))
# print(emp)

# operators
# print("d" + "o")
# print("d" * 3)


# iterate thru tuple, list and dictionary

# for d in days:
#     print(d)

# for j in junk:
#     print(type(j))

for name, email in emp.items():
    print(name, email)
