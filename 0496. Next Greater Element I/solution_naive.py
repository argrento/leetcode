class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        
        for num1 in nums1:
            offset = nums2.index(num1)
            greater_element = -1
            for idx, num2 in enumerate(nums2[offset:]):
                if num2 > num1:
                    greater_element = num2
                    break
            result.append(greater_element)
        
        return result
