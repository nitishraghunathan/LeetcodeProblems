class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
         1. Last day will never have a greater temperature
         2. Find the first day where temperature is greater than the temperature at the ith day
         3. we declare a results array where all elements are zero to handle error cases and edge cases
         4. We iterate the entire temperatures array and store elements in the stack
         5. The moment we find temperature greater than the top most element in the stack we pop and compute the index
         6. We store the index as well as the value in the stack
         7. we return the results array
        """
        result = [0]*len(temperatures)
        stack = []
        for index, value in enumerate(temperatures):
            while stack and stack[-1][1] < value:
                past_index, past_value = stack.pop()
                result[past_index] = index - past_index
            stack.append([index, value])
        return result