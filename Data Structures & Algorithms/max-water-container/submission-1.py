class Solution:
    def maxArea(self, heights: list[int]) -> int:
        n, best= len(heights), 0
        l, r = 0,n-1
        while l<r:
            height, widht = min(heights[l], heights[r]), r-l
            best = max(height*widht, best)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return best