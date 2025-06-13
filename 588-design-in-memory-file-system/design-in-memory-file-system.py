class FileSystem:

    def __init__(self):
        self.root = TrieNode('root')

    def ls(self, path: str) -> List[str]:
        if not path:
            return []
        paths = path.split('/')
        current = self.root
        result = []
        for path in paths:
            if path in current.subfiles:
                current = current.subfiles[path]
        if current.isFile:
            result.append(current.name)
        else:
            result.extend(current.subfiles.keys())
        return sorted(result)
        

    def mkdir(self, path: str) -> None:
        if not path:
            return
        paths = path.split('/')
        current = self.root
        result = []
        for path in paths:
            if path not in current.subfiles:
                current.subfiles[path] = TrieNode(path)    
            current = current.subfiles[path]
        current.isFile = False
        

    def addContentToFile(self, path: str, content: str) -> None:
        if not path:
            return
        paths = path.split('/')
        current = self.root
        result = []
        for path in paths:
            if path not in current.subfiles:
                current.subfiles[path] = TrieNode(path)    
            current = current.subfiles[path]
        current.isFile = True
        current.content += content

    def readContentFromFile(self, path: str) -> str:
        if not path:
            return []
        paths = path.split('/')
        current = self.root
        result = []
        for path in paths:
            if path in current.subfiles:
                current = current.subfiles[path]
            else:
                return "" 

        return current.content if current.isFile else ''
        
class TrieNode:
    def __init__(self, name):
        self.name = name
        self.isFile = False
        self.subfiles = {}
        self.content = ''


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)