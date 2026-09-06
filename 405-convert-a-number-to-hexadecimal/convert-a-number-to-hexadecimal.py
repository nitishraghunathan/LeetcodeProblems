class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        hex_map = {10:'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        string = ""
        if num < 0:
            num &= 0xFFFFFFFF
        while num > 0:
            remainder = num%16
            num = num//16
            if remainder in hex_map:
                string = hex_map[remainder] + string
            else:
                string = str(remainder) + string 
        return string
