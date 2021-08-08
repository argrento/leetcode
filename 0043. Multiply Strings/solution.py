class Solution:
    def add(self, num1: str, num2: str) -> str:
        max_num, min_num = (num1, num2) if len(num1) > len(num2) else (num2, num1)
        min_num = '0' * (len(max_num) - len(min_num)) + min_num
        carry = 0
        result = ''
        
        for a, b in zip(max_num[::-1], min_num[::-1]):
            r = ord(a) - 48 + ord(b) - 48 + carry
            carry = r // 10
            r = r % 10
            result += chr(r + 48)
        if carry:
            result += '1'
        return result[::-1]
        
    def multiply(self, num1: str, num2: str) -> str:
        result = '0'
        carry = 0
        for offset, n2 in enumerate(num2[::-1]):
            subresult = ''
            carry = 0
            for _, n1 in enumerate(num1[::-1]):
                r = (ord(n1) - 48) * (ord(n2) - 48) + carry
                carry = r // 10
                r = r % 10
                subresult = chr(r + 48) + subresult
            if carry:
                subresult = chr(carry + 48) + subresult
            subresult = subresult + '0' * offset
            result = self.add(result, subresult)
        
        result = result.lstrip('0')
        return '0' if not result else result