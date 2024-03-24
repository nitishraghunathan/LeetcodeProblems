class FreqStack:

    def __init__(self):
        self.map_dict = {}
        self.max_count = 0
        self.group = []
        

    def push(self, val: int) -> None:
        if val not in self.map_dict:
            self.map_dict[val] = 0
        self.map_dict[val] +=1
        if self.map_dict[val] > self.max_count:
            self.max_count = self.map_dict[val]
        if self.max_count > len(self.group):
            self.group.append([])
        self.group[self.map_dict[val]-1].append(val)        

    def pop(self) -> int:
       key = -1
       if self.group:
            key = self.group[self.max_count-1].pop()
       self.map_dict[key] -=1
       if self.map_dict[key] == 0:
            del self.map_dict[key]
       if not self.group[self.max_count-1]:
            self.group.pop()
            self.max_count-=1
       return key
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()