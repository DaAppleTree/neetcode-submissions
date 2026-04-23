class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ppa = [1]
        for i in range(len(nums)):
            ppa.append(nums[i] * ppa[-1])
        
        spa = [1]
        for i in range(len(nums)-1,-1,-1):
            spa.append(nums[i] * spa[-1])
        
        print(ppa,spa)
        newnums = []
        for i in range(len(nums)):
            newnums.append(ppa[i] * spa[len(spa)-i-2])
        return newnums