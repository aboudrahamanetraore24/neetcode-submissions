class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int] | None:
        if not nums: return None

        seen = dict()
        for i in range(len(nums)):
            if nums[i] in seen:
                return [seen[nums[i]], i]
            seen[target-nums[i]] = i
        return None