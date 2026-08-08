class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l,r, best = 0, len(heights)-1, 0
        while l<r:
            if heights[l]<=heights[r]:
                best = max(best, (r-l)*heights[l])
                l+=1
            else:
                best = max(best, (r-l)*heights[r])
                r-=1
        return best