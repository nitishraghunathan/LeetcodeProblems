class Solution:
    def confusingNumber(self, n: int) -> bool:
        def function_list(n:int):
            number_list = []
            if n == 0:
                return ["0"]
            while n > 0:
                number_list.insert(0, str(n%10))
                n = n//10
            return number_list
        map_dict = {"0" : "0", "1" : "1", "8": "8", "6" : "9", "9" : "6"}
        number_list = function_list(n)
        for index,number in enumerate(number_list):
            if number not in map_dict:
                return False
            number_list[index] = map_dict[number]
        return n != int("".join(number_list[::-1]))




        