class MyHashMap:

    def __init__(self):
        self.size = 2039
        self.map_dict = [Node(-1, -1) for _ in range(self.size)]

    def put(self, key: int, val: int) -> None:
        index = key%(self.size)
        head = self.map_dict[index]
        while head.next:
            if head.next.key == key:
                head.next.val = val
                return
            head = head.next
        head.next = Node(key, val)

    def get(self, key: int) -> int:
        index = key%(self.size)
        head = self.map_dict[index]
        while head:
            if head.key == key:
                return head.val
            head = head.next
        return -1
        
    def remove(self, key: int) -> None:
        index = key%(self.size)
        head = self.map_dict[index]
        while head:
            if head.next and head.next.key == key:
                head.next = head.next.next
                return
            head = head.next
        return
        

class Node:
    key: int
    val: int 
    next: Node 
    def __init__(self, key, val):
        self.key = key
        self.val = val 
        self.next = None
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)