class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        map_dict = {}
        def dfs(src, dest, visited, amount):
            if src==dest:
                return amount
            for values in map_dict[src]:
                if values[0] not in visited:
                    visited.add(values[0])
                    result = dfs(values[0], dest, visited, amount*values[1])
                    if result != float(-1):
                        return result
            return float(-1)
        for equation, value in zip(equations, values):
            if equation[0] not in map_dict:
                map_dict[equation[0]] = []
            map_dict[equation[0]].append([equation[1], value])
            if equation[1] not in map_dict:
                map_dict[equation[1]] = []
            new_value = 1/value if value != float(0) else value
            map_dict[equation[1]].append([equation[0], new_value])

            result = []
            for query in queries:
                if query[0] not in map_dict:
                    result.append(float(-1))
                    continue
                result.append(dfs(query[0], query[1], set(), float(1)))  
        return result

        