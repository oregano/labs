"""
Write a function that returns the elements on odd positions (0
based) in a list
"""
def solution(input):
    output = [input[i] for i in range(1, len(input)) if i % 2 != 0]
    print(output)
    return output
assert solution([0,1,2,3,4,5]) == [1,3,5]
assert solution([1,-1,2,-2]) == [-1,-2]
