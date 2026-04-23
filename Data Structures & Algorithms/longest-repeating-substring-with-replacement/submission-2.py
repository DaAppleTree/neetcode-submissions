class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        count = {}
        maxl, maxf = 0, 0
        for letter in letters:
            count[letter] = 0

        l, r = 0, 0
        while r < len(s):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])
            r += 1
            while (r-l) - maxf > k:
                count[s[l]] -= 1
                l += 1
            maxl = max(maxl, r-l)
        return maxl