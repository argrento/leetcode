class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                rightop, leftop = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(leftop + rightop)
                elif token == '-':
                    stack.append(leftop - rightop)
                elif token == '*':
                    stack.append(leftop * rightop)
                elif token == '/':
                    stack.append(int(leftop / rightop))
        
        return stack[0]
                
