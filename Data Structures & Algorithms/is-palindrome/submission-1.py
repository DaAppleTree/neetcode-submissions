class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()
        t = ""
        n = len(s)

        for i in range(n):
            if s[i] in allowed:
                t += s[i]

        n = len(t)
        if not t:
            return True
        for i in range(n//2+1):
            if t[i] != t[n-i-1]:
                return False
        return True