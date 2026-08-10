class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        max_seen = 0
        
        # Loop backwards through the string
        for char in reversed(s):
            val = roman_map[char]
            if val < max_seen:
                total -= val
            else:
                total += val
                max_seen = val
                
        return total