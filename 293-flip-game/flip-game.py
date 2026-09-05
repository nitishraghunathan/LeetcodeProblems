class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        result = []
        for i in range(1, len(currentState)):
            if currentState[i-1:i+1] == "++":
                new_state = "--" + currentState[i+1:]
                if i -2 > -1:
                    new_state = currentState[:i-1] + new_state
                result.append(new_state)
        return result
        