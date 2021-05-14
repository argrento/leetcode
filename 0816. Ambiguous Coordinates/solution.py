class Solution:
    def generate_float(self, s: str):
        if not s or len(s) > 1 and s[0] == s[-1] == '0': 
            return []
        if s[0] == '0':
            if len(s) == 1:
                return[s]
            else:
                return ['0.' + s[1:]]
        if s[-1] == '0':
            return [s]
        floats = [s]
        for idx in range(1, len(s)):
            floats.append(s[:idx] + '.' + s[idx:])
        return floats
    
    def ambiguousCoordinates(self, s: str) -> List[str]:
        result = []
        
        # remove brackets
        s = s[1:-1]
        
        for idx in range(len(s)):
            for left, right in itertools.product(self.generate_float(s[:idx]), 
                                                 self.generate_float(s[idx:])):
                result.append(f"({left}, {right})")
            
        return result
        
