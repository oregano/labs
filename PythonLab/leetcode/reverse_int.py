class Solution:
    def reverse_int(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)

        rev = 0
        while x > 0:
            t = x % 10 
            x = int(x / 10)
            rev = rev * 10 + t
        
        rev = rev * sign
        print(rev)
        print(2 ** 31 * sign)
        if rev > ( 2 ** 31 * sign):
            return 0
        return rev

if __name__ == "__main__":
    print(Solution().reverse_int(1))
    print(Solution().reverse_int(-2147483648))
    # print(Solution().reverse_int(4322))
    # print(Solution().reverse_int(-3201))