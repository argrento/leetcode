class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'{': '}', '[': ']', '(': ')'}
        stack = []
        
        for token in s:
            if token in brackets.keys():
                stack.append(token)
            elif stack and token == brackets[stack[-1]]:
                del stack[-1]
            else:
                return False
        if stack:
            return False
        return True