class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Construct the path without . or .. and to trailing /
        // are considered as single /
        1. Use a stack to store all the string characters 
        2. Whenever there is a single . just continue
        3. Whenever there is a .. we pop the latest element in the stack
        4. otherwise we just append elements to the stack
        5. we construct the final file path string with a leading / and join the elements of the stack
        """
        stack = []
        for portion in path.split("/"):
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == '.' or not portion:
                    continue
            else:
                    stack.append(portion)
        
        file_path = '/' + "/".join(stack)
        return file_path