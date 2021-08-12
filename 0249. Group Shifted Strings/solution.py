class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strings:
            key = tuple((ord(s[0]) - ord(c)) % 26 for c in s)
            result[key].append(s)
        return sorted(result.values())