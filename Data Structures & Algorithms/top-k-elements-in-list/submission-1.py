class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        arr = []
        for i in range(k):
            maxkey, maxvalue = 0, 0
            for key in count:
                if count[key] > maxvalue:
                    maxvalue = count[key]
                    maxkey = key
            
            arr.append(maxkey)
            del count[maxkey]
        return arr

            