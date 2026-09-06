class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.total_sum = 0
        self.queue = []
        

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            value = self.queue.pop(0)
            self.total_sum -= value
        self.total_sum += val
        self.queue.append(val)
        return self.total_sum/len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)