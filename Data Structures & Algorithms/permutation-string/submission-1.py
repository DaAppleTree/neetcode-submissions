class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count = [0] * 26
        for char in s1:
            count[ord(char)-ord("a")] += 1
        
        for i in range(len(s1)):
            count[ord(s2[i])-ord("a")] -= 1
            if count == [0] * 26:
                return True
        for i in range(len(s2)-len(s1)):
            l, r = i, i + len(s1)
            count[ord(s2[l])-ord("a")] += 1
            count[ord(s2[r])-ord("a")] -= 1
            if count == [0] * 26:
                return True
        return False
        