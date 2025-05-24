class MyQueue:

    def __init__(self):
        """
        1. Create two stacks for the queue
        2. During push put all elements one stack 
        3. During pop, pop all elements from the first stack to the other stack
        4. Return popped element
        """
        self.first_stack = []
        self.second_stack = []

    def push(self, x: int) -> None:
        self.first_stack.append(x)
        

    def pop(self) -> int:
        if self.second_stack:
            return self.second_stack.pop()
        while self.first_stack:
            self.second_stack.append(self.first_stack.pop())
        return self.second_stack.pop()
        

    def peek(self) -> int:
        if self.second_stack:
            return self.second_stack[-1]
        while self.first_stack:
            self.second_stack.append(self.first_stack.pop())
        return self.second_stack[-1]
        
    def empty(self) -> bool:
        return not self.first_stack and not self.second_stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()