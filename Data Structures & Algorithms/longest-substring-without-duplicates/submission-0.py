class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = set()
        q = deque()
        maximum = 0
        for i in range(len(s)):
            if s[i] not in x:
                x.add(s[i])
                q.append(s[i])
            else:
                n = deque.popleft(q)
                while n != s[i]:
                    x.remove(n)
                    n = deque.popleft(q)
                q.append(s[i])
            if len(q) > maximum:
                maximum = len(q)
        return maximum