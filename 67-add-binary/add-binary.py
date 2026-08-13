class Solution:
    def addBinary(self, a: str, b: str) -> str:
        b_len, a_len = len(b), len(a)
        if b_len > a_len:
            return self.addBinary(b,a)
        diff = a_len - b_len
        carry, new_str = 0, ""
        for i in range(a_len-1, -1, -1):
            if i-diff > -1:
                sum_val = int(a[i]) + int(b[i-diff]) + carry
            else:
                sum_val = int(a[i]) + carry

            carry = sum_val//2
            total_sum = sum_val%2
            new_str = str(total_sum) + new_str
            print(f"This is carry: {carry}")
            print(f"This is sum: {total_sum}")
        if carry > 0:
            new_str = str(carry) + new_str
        return new_str

           


