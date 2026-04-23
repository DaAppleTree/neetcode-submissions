class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        longest = 0
        count = {}
        for i in range(26):
            for letter in letters:
                count[letter] = 0
            l, r = 0, 0
            while r < len(s):
                count[s[r]] += 1
                r += 1
                while (r-l) - count[letters[i]] > k:
                    count[s[l]] -= 1
                    l += 1
                longest = max(longest, r-l)
        return longest