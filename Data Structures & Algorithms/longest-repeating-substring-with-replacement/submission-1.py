class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        maxl, maxf = 0, 0
        l = 0
        for r in range(len(s)):
            idx = ord(s[r]) - ord("A")
            count[idx] += 1
            maxf = max(maxf, count[idx])
            while (r-l+1) - maxf > k:
                count[ord(s[l]) - ord("A")] -= 1
                l += 1
            maxl = max(maxl, r-l+1)
        return maxl