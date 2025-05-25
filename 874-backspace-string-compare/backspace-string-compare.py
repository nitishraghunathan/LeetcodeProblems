class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        def get_string(string: str):
            stack = []
            for index, value in enumerate(string):
                if value == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(value)
            return "".join(stack)
        return get_string(s) == get_string(t)

                

        