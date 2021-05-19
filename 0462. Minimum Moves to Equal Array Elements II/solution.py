class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = sorted(nums)[len(nums) // 2]
        result = 0
        for num in nums:
            result += abs(num - median)
            
        return result
