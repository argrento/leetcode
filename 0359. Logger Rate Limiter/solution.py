class Logger:

    def __init__(self):
        self.history = {}
        self.delta = 10 # seconds

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.history:
            self.history[message] = timestamp
            to_print = True
        elif timestamp - self.history[message] < self.delta:
            to_print = False
        else:
            self.history[message] = timestamp
            to_print = True
        return to_print
