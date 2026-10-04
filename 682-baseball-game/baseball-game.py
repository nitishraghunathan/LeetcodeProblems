class Solution:
    def calPoints(self, operations: list[str]) -> int:
        result = []
        for operation in operations:
            match operation:
                case "+":
                    a = result[-1] if len(result) > 0 else 0
                    b = result[-2] if len(result) > 1 else 0
                    result.append(a+b)
                case "C":
                    result.pop()
                case "D":
                    a = result[-1]*2 if len(result) > 0 else 0
                    result.append(a)
                case _:
                    result.append(int(operation))
        return sum(result)
        