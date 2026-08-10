class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen, need, m, n, base = [0]*26, [0]*26, len(s1), len(s2), ord('a')
        if m > n:
            return False
        for i in range(m):
            need[ord(s1[i])-base]+=1
            seen[ord(s2[i])-base]+=1
        if need == seen:
            return True
        for i in range(m,n):
            seen[ord(s2[i-m])-base]-=1
            seen[ord(s2[i])-base]+=1
            if need == seen:
                return True
        return False