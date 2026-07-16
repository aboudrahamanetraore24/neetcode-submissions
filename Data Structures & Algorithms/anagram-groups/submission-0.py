class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = dict()
        for s in strs:
            freq_s = [0] * 26
            for c in s:
                freq_s[ord(c)-ord("a")] += 1
            freq_s = tuple(freq_s)
            if freq_s in d:
                d[freq_s].append(s)
            else:
                d[freq_s] = [s]
        return list(d.values())