class StringIterator:

    def __init__(self, compressedString: str):
        self.new_string = ""
        i = 0
        n = len(compressedString)
        
        while i < n:
            char = compressedString[i]
            i += 1
            
            # Find the multi-digit repeat count
            counter = i
            while counter < n and compressedString[counter].isdigit():
                counter += 1
            
            # Append the character repeated by the parsed count
            count = int(compressedString[i:counter])
            self.new_string += char * count
            
            # Advance index past the digits
            i = counter

        self.index = -1

    def next(self) -> str:
        if self.index + 1 < len(self.new_string):
            self.index += 1
            return self.new_string[self.index]
        return " "

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.new_string)