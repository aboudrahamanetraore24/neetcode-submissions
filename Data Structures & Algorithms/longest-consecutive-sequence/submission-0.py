class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set(nums)
        best = 0
        for x in seen:
            if (x-1) in seen:
                continue
            score = 1
            while x+1 in seen:
                score += 1
                x = x+1
            best = max(best, score)
        return best