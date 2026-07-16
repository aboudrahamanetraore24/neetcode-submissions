class Solution:
    def encode(self, strs: list[str]) -> str:
        out=""
        for s in strs:
            out+=str(len(s))+"#"+s
        return out
    def decode(self, s: str) -> list[str]:
        n = len(s)
        out = []
        if not s:
            return out
        cur = 0
        while cur<n:
            j = cur
            while s[j]!='#': 
                j+=1
            shift = int(s[cur:j])
            start = j+1
            end = start + shift
            out.append(s[start:end])
            cur = end
        return out