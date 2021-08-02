class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        
        for idx, num in enumerate(nums):
            val = target - num
            if val not in h:
                h[num] = idx
            else:
                return [h[val], idx]
                