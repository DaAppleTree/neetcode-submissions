import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums

        maximum = []
        res = []
        
        for i in range(k):
            heapq.heappush(maximum, -nums[i])
        maxval = heapq.heappop(maximum)
        heapq.heappush(maximum, maxval)
        res.append(-maxval)

        for i in range(n-k):
            heapq.heappush(maximum, -nums[i+k])
            maxval = heapq.heappop(maximum)
            if -maxval == nums[i] and (i+k+1 == n or -maxval != nums[i+k+1]):
                while -maxval not in nums[i+1:i+k+1]:
                    maxval = heapq.heappop(maximum)
            heapq.heappush(maximum, maxval)
            res.append(-maxval)
        return res