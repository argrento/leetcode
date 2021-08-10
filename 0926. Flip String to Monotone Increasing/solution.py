class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zero_counter = s.count('0')
        one_counter = 0
        result = len(s) - zero_counter
        
        for idx, symbol in enumerate(s):
            if symbol == '0':
                zero_counter -= 1
            elif symbol == '1':
                result = min(result, zero_counter + one_counter)
                one_counter += 1
        
        return result