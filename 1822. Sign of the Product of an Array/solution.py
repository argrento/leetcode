class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                result *= -1
        
        return result
