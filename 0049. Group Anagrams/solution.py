class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(s))
            result[key].append(s)
        
        return result.values()
