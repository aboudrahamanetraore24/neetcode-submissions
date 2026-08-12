class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n, base = len(s1), len(s2), ord('a')
        if m > n:
            return False
        need, seen = [0]*26, [0]*26
        for i in range(m):
            need[ord(s1[i])-base] += 1
            seen[ord(s2[i])-base] += 1
        matches = sum(need[c] == seen[c] for c in range(26))

        for i in range(m, n):
            if matches == 26:
                return True
            inc, out = ord(s2[i])-base, ord(s2[i-m])-base
            seen[inc] += 1
            if seen[inc] == need[inc]:
                matches += 1
            elif seen[inc] == need[inc] + 1:
                matches -= 1
            seen[out] -= 1
            if seen[out] == need[out]:
                matches += 1
            elif seen[out] == need[out] - 1:
                matches -= 1

        return matches == 26