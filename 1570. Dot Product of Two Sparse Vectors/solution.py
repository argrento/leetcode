class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzero = {}
        for idx, n in enumerate(nums):
            if n != 0:
                self.nonzero[idx] = n
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for idx in self.nonzero:
            if idx in vec.nonzero:
                result += self.nonzero[idx] * vec.nonzero[idx]
        
        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)