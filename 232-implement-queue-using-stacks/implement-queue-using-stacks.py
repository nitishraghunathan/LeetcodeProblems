class MyQueue:

    def __init__(self):
        self.stack_one = []
        self.stack_two = []

    def push(self, x: int) -> None:
        self.stack_one.append(x)

    def pop(self) -> int:
        while self.stack_one:
            self.stack_two.append(self.stack_one.pop())
        print(self.stack_two)
        val = self.stack_two.pop() if self.stack_two else -1
        while self.stack_two:
            self.stack_one.append(self.stack_two.pop())
        return val

    def peek(self) -> int:
        while self.stack_one:
            self.stack_two.append(self.stack_one.pop())
        val = self.stack_two[-1] if self.stack_two  else -1
        while self.stack_two:
            self.stack_one.append(self.stack_two.pop())
        return val

    def empty(self) -> bool:
        return len(self.stack_one) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()