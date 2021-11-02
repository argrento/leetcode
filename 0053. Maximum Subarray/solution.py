class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        sum = nums[0]
        del nums[0]
        
        for num in nums:
            sum = max(num, sum + num)
            if sum > max_sum:
                max_sum = sum
        
        return max_sum
