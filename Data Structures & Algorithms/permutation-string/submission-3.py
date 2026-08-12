class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool | int:
        m, n , need, seen, matches = len(s1), len(s2), [0]*26, [0]*26, 0
        if m > n:
            return False
        base = ord('a')
        for i in range(m):
            need[ord(s1[i])-base]+=1
            seen[ord(s2[i])-base]+=1
        matches = sum(need[i]==seen[i] for i in range(26))
        for i in range(m,n):
            if matches == 26:
                return True
            out, inn = ord(s2[i-m])-base, ord(s2[i])-base

            if seen[out] == need[out]:
                matches-=1
            seen[out]-=1
            if seen[out] == need[out]:
                matches+=1

            if seen[inn] == need[inn]:
                matches-=1
            seen[inn]+=1
            if seen[inn] == need[inn]:
                matches+=1

        return matches == 26