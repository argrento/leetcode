class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                rightop, leftop = stack.pop(), stack.pop()
                stack.append(int(eval(f"{leftop}{token}{rightop}")))
        
        return stack[0]
