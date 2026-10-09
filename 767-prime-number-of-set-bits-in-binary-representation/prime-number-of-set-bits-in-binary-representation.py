class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def set_prime(num):
            if num < 2:
                return False
            i = 2
            while i*i <= num:
                if i!= num and num%i == 0:
                    return False
                i+=1
            print(f"prime_number: {num}")
            return True
        def set_bit(num):
            counter = 0
            sum_num = num 
            while num > 0:
                if num%2==1:
                    counter+=1
                num = num//2
            print(f"counter:{counter}, num: {sum_num} ")
            return set_prime(counter)
        set_count = 0
        for index in range(left, right+1):
            if set_bit(index):
                set_count +=1
                
        return set_count
        