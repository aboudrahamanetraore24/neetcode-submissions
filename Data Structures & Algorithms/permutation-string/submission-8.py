class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n, base = len(s1), len(s2), ord('a')
        if m > n:
            return False

        need, seen = [0]*26, [0]*26
        for i in range(m):
            need[ord(s1[i])-base] += 1
            seen[ord(s2[i])-base] += 1

        matches = sum(1 for i in range(26) if need[i] == seen[i])
        if matches == 26:
            return True

        for i in range(m, n):
            out, inn = ord(s2[i-m])-base, ord(s2[i])-base

            # retirer le caractère qui sort de la fenêtre
            if seen[out] == need[out]:
                matches -= 1
            seen[out] -= 1
            if seen[out] == need[out]:
                matches += 1

            # ajouter le caractère qui entre dans la fenêtre
            if seen[inn] == need[inn]:
                matches -= 1
            seen[inn] += 1
            if seen[inn] == need[inn]:
                matches += 1

            if matches == 26:
                return True

        return False