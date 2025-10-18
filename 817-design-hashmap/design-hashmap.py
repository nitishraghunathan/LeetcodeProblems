class MyHashMap:

    def __init__(self):
        self.map = {}
        

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            self.map[key] = 0
        self.map[key] = value
        return

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        return self.map[key]
        

    def remove(self, key: int) -> None:
        if key in self.map:
            self.map.pop(key)
        return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)