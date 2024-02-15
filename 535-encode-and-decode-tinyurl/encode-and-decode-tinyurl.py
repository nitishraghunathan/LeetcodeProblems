class Codec:
    def __init__(self):
        self.map_dict = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        value = 'https://tinyurl/' + str(hash(longUrl))
        self.map_dict[value] = longUrl
        return value 

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.map_dict[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))