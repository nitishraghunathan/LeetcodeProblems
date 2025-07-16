class HitCounter:

    def __init__(self):
        self.queue = []

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        lower_limit = timestamp-300
        left, right = 0, len(self.queue)-1
        while left <= right:
            mid = left + (right-left)//2
            if self.queue[mid] <= lower_limit:
                left = mid+1
            else:
                right = mid-1
        return len(self.queue)-left
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)