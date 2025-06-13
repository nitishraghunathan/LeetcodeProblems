class FreqStack:

    def __init__(self):
        self.map_dict = {}
        self.group_list = []
        self.max_size = 0
        

    def push(self, val: int) -> None:
        if val not in self.map_dict:
            self.map_dict[val] = 0
        self.map_dict[val] += 1
        if self.map_dict[val] > self.max_size:
            self.group_list.append([])
            self.max_size = self.map_dict[val]
        self.group_list[self.map_dict[val]-1].append(val)

    def pop(self) -> int:
       if not self.group_list:
            return -1
       val = self.group_list[self.max_size-1].pop()
       if not self.group_list[self.max_size-1]:
          self.group_list.pop()
          self.max_size -=1
       self.map_dict[val] -=1
       if self.map_dict[val] == 0:
          self.map_dict.pop(val)
       return val



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()