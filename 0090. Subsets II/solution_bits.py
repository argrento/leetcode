class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        max_selector = 2 ** len(nums)
        
        # zero already in result
        for selector in range(1, max_selector):
            bitfield = selector
            subresult = []
            idx = 0
            while bitfield != 0:
                if bitfield & 1 == 1:
                    subresult.append(nums[idx])
                bitfield = bitfield >> 1
                idx += 1
            subresult = sorted(subresult)
            if subresult not in result:
                result.append(subresult)
            
        return result