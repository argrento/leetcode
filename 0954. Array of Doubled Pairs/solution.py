class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        values = collections.Counter(arr)
        
        for v in sorted(arr, key=abs):
            if values[v] == 0:
                continue
            if values[2*v] == 0:
                return False
            values[v] -= 1
            values[2*v] -= 1
        return True