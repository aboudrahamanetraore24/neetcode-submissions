class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        prefix = []
        prefix.append(1)
        for i in range(1,n):
            prefix.append(nums[i-1]*prefix[i-1])

        suffix = [1]*n
        for i in range(1,n):
            suffix[n-i-1] = suffix[n-i]*nums[n-i]
        
        out = []
        for i in range(n):
            out.append(prefix[i]*suffix[i])
    
        return out
    