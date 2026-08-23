class Solution:
    def isHappy(self, n: int) -> bool:
        tracker = set()
        number = str(n)
        while True:
            if number == "1":
                return True
            if number in tracker:
                return False
            tracker.add(number)
            total_sum = 0
            for i in range(len(number)):
                total_sum += int(number[i])**2
            number = str(total_sum)
        return False