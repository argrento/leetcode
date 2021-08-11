class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        maximums = [nums[0]] # from the left
        minimums = [0] * len(nums) # from the right
        min_n = nums[-1]
        result = 0
        
        for n in nums[1::]:
            maximums.append(max(maximums[-1], n))
            
        for idx in range(len(nums)-1, -1, -1):
            min_n = min(min_n, nums[idx])
            minimums[idx] = min_n
            
            if nums[idx] == maximums[idx] and nums[idx] == minimums[idx]:
                result += 1
        
        return result