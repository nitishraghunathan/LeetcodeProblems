class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        1. Add all the buses for every stop in a set.
        2. use bfs add the source bus stop
        3. Have a visited set to add the buses travelled and check if bus has beem taken
        4. Have a counter to calculate the number of buses needed to reach the target
        """
        bus_dict = {}
        for index, route in enumerate(routes): 
            for stop in route:
                if stop not in bus_dict:
                    bus_dict[stop] = set()
                bus_dict[stop].add(index)
        visited = set()
        queue = []
        queue.append(source)
        bus_no = 0
        while queue:
            size = len(queue)
            for i in range(size):
                stop = queue.pop(0)
                if target == stop:
                    return bus_no
                for bus in bus_dict.get(stop,[]):
                    if bus not in visited:
                        visited.add(bus)
                        queue.extend(routes[bus])
            bus_no +=1
        return -1
                