class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.right, self.left = Node(0, 0), Node(0, 0)
        self.right.prev, self.left.next = self.left, self.right
        
    def insert(self, node):
        prev, next = self.right.prev, self.right
        node.next, node.prev = next, prev
        prev.next, next.prev = node, node
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = node
            self.insert(node)
            return 
        if len(self.cache) == self.capacity:
            lru_node = self.left.next
            self.remove(lru_node)
            self.cache.pop(lru_node.key)
        self.insert(node)
        self.cache[key] = node
        
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)