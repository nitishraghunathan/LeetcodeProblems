class MyHashSet:

    def __init__(self):
        self.size = 2039
        self.map_dict = [Node(-1)]*2039

    def add(self, key: int) -> None:
        index = key%self.size
        head = self.map_dict[index]
        while head.next:
            head = head.next
        head.next = Node(key)

    def remove(self, key: int) -> None:
        index = key%self.size
        head = self.map_dict[index]
        while head:
            if head.next and head.next.key == key:
                head.next = head.next.next
            head = head.next
    def contains(self, key: int) -> bool:
        index = key%self.size
        head = self.map_dict[index]
        while head:
            if head.key == key:
                return True
            head = head.next 
        return False
        
class Node:
    key:int
    next: Node
    def __init__(self, key):
        self.key = key
        self.next = None


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)