class Codec:
    def __init__ (self):
        self.map_dict = {}

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        hash_code = hash(''.join(strs))
        self.map_dict[hash_code] = strs
        return hash_code
        
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if s in self.map_dict:
            return self.map_dict[s]
        return ""


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))