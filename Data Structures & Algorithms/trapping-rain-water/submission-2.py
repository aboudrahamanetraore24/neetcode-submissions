class Solution:
    def trap(self, height: list[int]) -> int:
        n, total = len(height), 0
        l, r = 0, n-1
        while l<r:
            if height[l]<=height[r]:
                l_max= l+1
                while l_max < n and height[l_max]<height[l]:
                    l_max+=1
                for i in range(l+1,l_max):
                    total+=height[l]-height[i]
                l = l_max
            else:
                r_min= r-1
                while r_min >= 0 and height[r_min]<height[r]:
                    r_min-=1
                for i in range(r, r_min, -1):
                    total+=height[r]-height[i]
                r= r_min
        return total