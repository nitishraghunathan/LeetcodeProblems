class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        new_str = ""
        def create_string(string: str):
            new_string = ""
            skip = 0
            for index in range(len(string)-1, -1, -1):
                if string[index] == "#":
                    skip +=1
                elif skip > 0:
                    skip -=1
                    continue
                else:
                    new_string += string[index]
            return new_string
        return create_string(s) == create_string(t)


                

        