# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Reader4:
    def __init__(self):
        self.b4 = ['', '', '', '']
        self._renew()
        self.pointer = 0
        
    def _renew(self):
        # try to read 4 new bytes
        self.size = read4(self.b4)
        self.buffer_empty = True if self.size == 0 else False
    
    def get(self) -> str:
        if self.buffer_empty:
            # buffer is empty, can not read anything
            return None
        # buffer has at least 1 symbol
        symbol = self.b4[self.pointer]
        self.pointer += 1
        
        # buffer ended, read new
        if self.pointer == self.size:
            self._renew()
            self.pointer = 0
        return symbol

class Solution:
    def __init__(self):
        self.reader4 = Reader4()
    def read(self, buf: List[str], n: int) -> int:
        read_size = 0
        for idx in range(n):
            ch = self.reader4.get()
            if ch:
                buf[idx] = ch
                read_size += 1
            else:
                return read_size
            
        return read_size