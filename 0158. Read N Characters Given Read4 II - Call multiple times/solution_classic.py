# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.q = collections.deque()
    def read(self, buf: List[str], n: int) -> int:
        total = 0
        
        while total < n:
            if self.q:
                buf[total] = self.q.pop()
                total += 1
            else:
                tmp = [''] * 4
                count = read4(tmp)
                if not count:
                    break
                for i in range(count):
                    self.q.appendleft(tmp[i])
        
        return total
