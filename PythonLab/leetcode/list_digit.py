"""
Write a function that takes a number and returns a list of its
digits
"""
def solution(input):
    output = []

    while input > 0:
        output.append(input % 10)
        input = input // 10
    return output[::-1]
if __name__ == "__main__":
    print(solution(123))
#assert solution(123) == [1,2,3]
#assert solution(400) == [4,0,0]
