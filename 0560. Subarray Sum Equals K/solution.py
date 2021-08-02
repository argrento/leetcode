class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        hm = {0: 1}
        summ = 0
        for idx in range(len(nums)):
            summ += nums[idx]
            if summ - k in hm:
                result += hm[summ-k]
            hm[summ] = hm.get(summ, 0) + 1
        return result
        
