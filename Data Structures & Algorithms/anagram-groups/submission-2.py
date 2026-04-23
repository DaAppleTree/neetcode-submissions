class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = dict()
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        
        for c in t:
            if c in count and count[c] > 0:
                count[c] -= 1
                if count[c] == 0:
                    del count[c]
            else:
                return False
        
        if len(count) == 0:
            return True
        return False
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new = []
        for s in strs:
            found = False
            for i in range(len(new)):
                if self.isAnagram(new[i][-1],s):
                    new[i].append(s)
                    found = True
                    break
            if not found:
                new.append([s])
        return new

        