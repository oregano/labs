# list1 = [1, 4, 6, 8, 9]
# list2 = [3, 5, 7, 8, 10]


# def sum(x, y):
#     return x + y


# print(list(map(sum, list1, list2)))

# print(['a', 'b', 'c'] + [1, 2, 3])


# sort using map

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

sorted_arr = sorted(arr)

print(sorted_arr[-2])
