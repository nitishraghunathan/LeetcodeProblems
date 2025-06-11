class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Requirements: 
        String: s 
        Substring to match: t
        Problem: Find minimum number of characters in S to match substring t
        ALgorithm: Two pointer approach + map 
        1. Have two maps:
            a. Store the elements of t in the map
            b. Store a new map which keeps track of the elements in the substring interation in S.
            c. Compare the two maps and once they are equal return the minimum substring
        2. Increase the pointer consistently till we reach the end.
        3. keep track of size and minimum substring
        """
        def check_map(tracking_map: dict, substring_map: dict) -> bool:
            for key, value in substring_map.items():
                if key not in tracking_map or value > tracking_map[key]:
                    return False
            return True

        left = 0
        right = len(s)
        index = 0
        min_substring = ""
        min_size = float('inf')
        substring_map = {}
        tracking_map = {}
        for item in t:
            if item not in substring_map:
                substring_map[item] = 0
            substring_map[item] +=1 
        front_pointer = 0
        while left < right:
            if s[left] not in  tracking_map:
                tracking_map[s[left]] = 0
            tracking_map[s[left]] +=1
            front_pointer = index
            left += 1
            while check_map(tracking_map, substring_map):
                if left - front_pointer <= min_size:
                    min_size = left - front_pointer
                    min_substring = s[front_pointer : left]
                   
                tracking_map[s[front_pointer]] -= 1
                if tracking_map[s[front_pointer]] == 0:
                    tracking_map.pop(s[front_pointer])
                front_pointer +=1
                index = front_pointer
        return min_substring
                

                


    
