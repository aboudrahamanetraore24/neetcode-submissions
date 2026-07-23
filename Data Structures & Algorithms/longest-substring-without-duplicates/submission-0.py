class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n, l, best = len(s), 0, 0
        seen = set()

        for r in range(n):
            while l<r and s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            best = max(best, r-l+1)
        return best