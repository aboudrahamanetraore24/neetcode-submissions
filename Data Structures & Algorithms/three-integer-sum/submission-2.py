class Solution:
    def twoSum(self, nums: list[int], target: int, start: int) -> list[list[int]]:
        n = len(nums)
        l, r = start + 1, n - 1
        outs = []
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                outs.append([l, r])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            elif s < target:
                l += 1
            else:
                r -= 1
        return outs

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        outs = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            double_outs = self.twoSum(nums, -nums[i], i)
            for d in double_outs:
                outs.append([nums[i], nums[d[0]], nums[d[1]]])
        return outs