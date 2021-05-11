class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                stack, leftop, rightop = stack[:-2], stack[-2], stack[-1] 
                stack.append(eval(f"int({leftop}{token}{rightop})"))
        
        return stack[0]
