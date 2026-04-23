class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        sol = ""
        for c in t:
            count[c] = count.get(c,0)-1
        
        l = 0
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            
            valid = True
            for c in count:
                if count[c] < 0:
                    valid = False
                    break
            
            while valid:
                if s[l] in count:
                    count[s[l]] -= 1
                if (r-l) < len(sol) or sol == "":
                    sol = s[l:r+1]
                l += 1
                for c in count:
                    if count[c] < 0:
                        valid = False
                        break
        return sol
