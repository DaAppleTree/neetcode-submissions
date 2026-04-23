class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxH = max(heights)
        maxW = 0
        while l < r:
            if (r-l)*maxH <= maxW:
                break
            else:
                w = (r-l) * min(heights[l], heights[r])
                if w > maxW:
                    maxW = w
                if heights[l] < heights[r]:
                    l += 1
                else:
                    r -= 1
        return maxW