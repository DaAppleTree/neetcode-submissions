class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        res, cur = 0, 1
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                continue
            elif nums[i+1] - 1 == nums[i]:
                cur += 1
            else:
                res = max(res, cur)
                cur = 1
        return max(res, cur)
        