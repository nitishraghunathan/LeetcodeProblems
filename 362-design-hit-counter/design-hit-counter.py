class HitCounter:

    def __init__(self):
        self.queue = []
        

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        lower_limit  = timestamp-300
        counter = 0
        for i in range(len(self.queue)):
            if self.queue[i] > timestamp:
                return counter
            elif lower_limit < self.queue[i] <= timestamp:
                counter+=1
        return counter
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)