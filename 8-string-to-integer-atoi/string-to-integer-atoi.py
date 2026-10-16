class Solution:
    def myAtoi(self, s: str) -> int:
        
        def remove_whitespaces(s:str):
            return s.strip()
        
        def remove_leading_zeros(s:str):
            left = 0
            while left < len(s) and  s[left] == 0: 
                left +=1
            return s[left:]
        def rounding_off(s:int, signed:bool):
            s = s if not signed else -s
            if s > 2**31-1:
                return 2**31-1
            elif s < -2**31:
                return -2**31
            return s
        def retrieve_sign(s:str):
            left = 0
            sign = False
            not_valid = False
            signed_int = {"+", "-"}
            while left < len(s) and s[left] in signed_int:
                if s[left] == '-':
                    sign = True
                left +=1
            if left > 1:
                not_valid = True
                return sign, True, s
            return sign, not_valid, s[left:]
            
        s = remove_whitespaces(s)
        s = remove_leading_zeros(s)
        signed, not_valid, s = retrieve_sign(s)
        print(f"This is {s}, signed: {signed}, not_valid: {not_valid}")
        if not_valid:
            return 0 
        accumulated_integer = 0
        for i in range(0, len(s)):
            print(f"This is s: {s} and accumulated_integer: {accumulated_integer}")
            if not s[i].isdigit():
                return rounding_off(accumulated_integer, signed)
            else:
                accumulated_integer = 10*accumulated_integer + (ord(s[i]) - ord('0'))
        return rounding_off(accumulated_integer, signed)





        