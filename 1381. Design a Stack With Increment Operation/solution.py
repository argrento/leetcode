class CustomStack:

    def __init__(self, maxSize: int):
        self.limit = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.limit:
            self.stack.append(x)

    def pop(self) -> int:
        val = -1
        if len(self.stack) != 0:
            val = self.stack[-1]
            del self.stack[-1]
        return val

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.stack))
        for idx in range(k):
            self.stack[idx] += val
