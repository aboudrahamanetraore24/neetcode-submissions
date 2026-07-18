class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = [c.lower() for c in s if c.isalnum()]
        n = len(s_cleaned)
        for i in range(n//2):
            if s_cleaned[i] != s_cleaned[n-1-i]:
                return False
        return True