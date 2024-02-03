class MovingAverage:

    def __init__(self, size: int):
        self.queue = []
        self.size = size
        self.total_val = 0

    def next(self, val: int) -> float:
        if len(self.queue)== self.size:
            returned = self.queue.pop(0)
            self.total_val -= returned
        self.queue.append(val)
        self.total_val += val
        return self.total_val/len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)