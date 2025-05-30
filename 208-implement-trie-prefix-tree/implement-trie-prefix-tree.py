class Trie:

    def __init__(self):
        self.root = TrieNode("/")
    
    def insert(self, word: str) -> None:
        current = self.root
        for index,value in enumerate(word):
            if value not in current.map_dict:
                current.map_dict[value] = TrieNode(value)
            current = current.map_dict[value]
        current.is_word = True
    
    def search(self, word: str) -> bool:
        current = self.root
        for index,value in enumerate(word):
            if value not in current.map_dict:
                return False
            else:
                current = current.map_dict[value]
        return current.is_word

    def startsWith(self, word: str) -> bool:
        current = self.root
        for index,value in enumerate(word):
            if not current:
                return False
            elif value not in current.map_dict:
                return False
            else:
                current = current.map_dict[value]
        return True
        
class TrieNode:
    def __init__(self, alphabet):
        self.char = alphabet
        self.map_dict = {}
        self.is_word = False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)