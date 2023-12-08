class Codec:
    def __init__(self):
        self.map_dict={}
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = hash(''.join(strs))
        self.map_dict[encoded_str] = strs
        return encoded_str
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return self.map_dict[s]
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))