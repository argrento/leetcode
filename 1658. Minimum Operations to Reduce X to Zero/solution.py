class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        
        hm = {0: -1}
        result = float(-inf)
        summ = 0
        
        for idx, num in enumerate(nums):
            summ += num
            if summ-target in hm:
                result = max(result, idx - hm[summ-target])
            
            hm[summ] = idx
        return -1 if result == float(-inf) else len(nums) - result
