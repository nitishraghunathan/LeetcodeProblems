class FreqStack:
    def __init__(self):
        self.number_dict = {}
        self.frequency_counter = [[]]

    def push(self, val: int) -> None:
        number_dict = self.number_dict
        frequency_counter = self.frequency_counter 
        if val not in number_dict:
            number_dict[val] = 0
        number_dict[val] += 1
        if number_dict[val] > len(frequency_counter)-1:
            frequency_counter.append([])
        frequency_counter[number_dict[val]].append(val)
    def pop(self) -> int:
        number_dict = self.number_dict
        frequency_counter = self.frequency_counter 
        length = len(frequency_counter)
        if  length== 1:
            return -1
        val =-1
        if len(frequency_counter[length-1]) > 0:
            val = frequency_counter[length-1].pop()
            number_dict[val] -=1
            if number_dict[val] == 0:
                number_dict.pop(val)
        if not frequency_counter[length-1]:
            frequency_counter.pop()
        return val
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()