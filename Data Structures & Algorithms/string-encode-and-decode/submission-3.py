class Solution:

    def encode(self, strs: List[str]) -> str:
        longstr = ""
        for s in strs:
            longstr += f"{len(s)}#{s}"
        return longstr

    def decode(self, s: str) -> List[str]:
        i = 0
        arr = []
        count = ""
        while i < len(s):
            if s[i] == "#":
                arr.append(s[i+1:i+int(count)+1])
                i += int(count) + 1
                count = ""
            else:
                count += s[i]
                i += 1
        return arr

