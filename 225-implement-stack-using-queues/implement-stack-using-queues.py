class MyStack:

    def __init__(self):
        self.first_queue = []

    def push(self, x: int) -> None:
        self.first_queue.append(x)

    def pop(self) -> int:
        if not self.first_queue:
            return -1
        return self.first_queue.pop()
    def top(self) -> int:
        if not self.first_queue:
            return -1
        return self.first_queue[-1]

    def empty(self) -> bool:
        return not self.first_queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()