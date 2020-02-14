class Solution:
    def rob(self, nums = list) -> int:
        if len(nums) == 0:
            return 0
        
        total = nums[0]
        for i in range(1, len(nums)):
            if i % 2 == 0 and i <= len(nums):
                total = total + nums[i]
        return total
        
if __name__ == "__main__":
    print(Solution.rob([1, 2]))
    