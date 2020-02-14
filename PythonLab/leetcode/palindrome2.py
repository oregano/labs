class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                print(one)
                print(two)
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True
        # n = len(s)
        # first = s[:int(n/2):1]
        # last = s[:int(n/2):-1]

        # if first == last:
        #     print(first, ' ', last)
        #     return True
        # else:
        #     for i in range(n):
        #         t = s[0:i] + s[i + 1:n]
        #         print(t)
        #         m = len(t)
        #         first = t[0:int(m/2):1]
        #         last = t[m:int(m/2)+1:-1]
        #         if m % 2 == 0:
        #             last = t[m:int(m/2)-1:-1]
                
        #         print(first, ' ', last)
        #         if first == last:
        #             return True
        #     return False
        

if __name__ == "__main__":
    # print(Solution().validPalindrome(s = 'abcba'))
    print(Solution().validPalindrome(s = 'abca'))
    # print(Solution().validPalindrome(s = 'deeee'))