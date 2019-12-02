list1 = [1, 4, 6, 8, 9]
list2 = [3, 5, 7, 8, 10]


def sum(x, y):
    return x + y


print(list(map(sum, list1, list2)))

print(['a', 'b', 'c'] + [1, 2, 3])
