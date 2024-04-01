# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
"""
How to store the the location
"""
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = [[-1,0], [0,1], [1,0],[0,-1]]
        visited = set()
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        def backtrack(i, j, dir):
            visited.add((i,j))
            robot.clean()
            for direct in range(4):
                new_direct = (direct + dir)%4
                x = i + directions[new_direct][0] 
                y = j + directions[new_direct][1]
                if (x,y) not in visited and robot.move():
                    backtrack(x,y, new_direct)
                    go_back()
                robot.turnRight()
        backtrack(0,0,0)