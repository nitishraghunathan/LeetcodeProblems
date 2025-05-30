class RandomizedSet:

    def __init__(self):
        self.map_dict = {}
        self.map_list = []
        

    def insert(self, val: int) -> bool:
        if val not in self.map_dict:
            self.map_list.append(val)
            self.map_dict[val] = len(self.map_list)-1
            return True
        return False

        

    def remove(self, val: int) -> bool:
        if val in self.map_dict:
            self.map_list.remove(val)
            self.map_dict.pop(val)
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.map_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()