class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""
        need, seen = [0]*128, [0]*128
        for i in range(n):
            need[ord(t[i])] += 1
            seen[ord(s[i])] += 1
        matches = sum(1 for c in range(128) if seen[c] >= need[c])
        best, best_l, best_r, l = m+1, None, None, 0
        if matches == 128:
            best, best_l, best_r = n, 0, n-1
        for r in range(n, m):
            c = ord(s[r])
            seen[c] += 1
            if seen[c] == need[c]:
                matches += 1
            while matches == 128:
                if r-l+1 < best:
                    best, best_l, best_r = r-l+1, l, r
                c = ord(s[l])
                if seen[c] == need[c]:
                    matches -= 1
                seen[c] -= 1
                l += 1
        return s[best_l:best_r+1] if best <= m else ""