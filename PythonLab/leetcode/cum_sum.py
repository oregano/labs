"""
Write a function that returns the cumulative sum of elements in a
list
"""
"""def solution(input):
    # time complexity O(n2)
    # space complexity O(n2)
    output = []
    for i in range(len(input)):
        sum = 0
        for j in range(0, i + 1):
            sum += input[j]
        output.append(sum)
    print(output)
    return output"""

# O(n) complexity
def solution(input):
    sums = dict()
    sums[0] = input[0]
    output = [input[0]]

    for i in range(1, len(input)):
        sums[i] = sums[i - 1] + input[i]
        output.append(sums[i])
    return output

 
assert solution([1,1,1]) == [1,2,3]
assert solution([1,-1,3]) == [1,0,3]
assert solution([1,-1,3, 2, 4, 6, 7, 8, 9, 9, 10]) == [1,0,3, 5, 9, 15, 22, 30, 39, 48, 58]