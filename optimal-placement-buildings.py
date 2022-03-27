
'''
Given a grid with w as width, h as height. Each cell of the grid represents a potential building lot and we will be adding "n" buildings inside this grid. The goal is for the furthest of all lots to be as near as possible to a building. Given an input n, which is the number of buildings to be placed in the lot, determine the building placement to minimize the distance the most distant empty lot is from the building. Movement is restricted to horizontal and vertical i.e. diagonal movement is not required.

For example, w=4, h=4 and n=3. An optimal grid placement sets any lot within two unit distance of the building. The answer for this case is 2.

"0" indicates optimal building placement and in this case the maximal value of all shortest distances to the closest building for each cell is "2".

1 0 1 2

2 1 2 1

1 0 1 0

2 1 2 1
'''

from collections import deque
import copy

class solution():
    def __init__(self):
        self.grid = None
        self.solgrid = None
        self.w = 0
        self.h = 0
        self.n = 0
        self.min = float("inf")
    
    def bfs(self):
        queue = deque()
        maxm = float("-inf")
        visited = [[-1 for i in range(self.w)] for j in range(self.h)]
        
        for i in range(self.h):
            for j in range(self.w):
                if self.grid[i][j] == "0":
                    queue.append((i, j, 0))
        
        while queue:
            x, y, dist = queue.popleft()
            dirs = [(0,1), (1, 0), (-1, 0), (0, -1)]
            
            for dir in dirs:
                newx = x + dir[0]
                newy = y + dir[1]
                
                if newx >=0 and newx < self.h and newy >=0 and newy < self.w and visited[newx][newy] == -1:
                    queue.append((newx, newy, dist + 1))
                    visited[newx][newy] = 1
                    maxm = max(maxm, dist + 1)
                    
        if maxm < self.min:
            self.min = maxm
            self.solgrid = copy.deepcopy(self.grid)
                
    def backtrack(self, n, r, c):
        if n == 0:
            self.bfs()
            return
             
        if c > self.w:
            r = r + 1
            c = 0
        
        # print(n, self.grid)
        
        for i in range(r, self.h):
            for j in range(c, self.w):
                if self.grid[i][j] == "*":
                    self.grid[i][j] = "0"
                    self.backtrack(n - 1, i, j + 1)
                    self.grid[i][j] = "*"
            
    def optimalPlacement(self, w, h, n):
        if not n:
            return 0
        
        self.n = n
        self.h = h
        self.w = w
        self.grid = [["*" for i in range(w)] for j in range(h)]
        
        self.backtrack(self.n, 0, 0)

sol = solution()
sol.optimalPlacement(4, 4, 3)
print(sol.min)
print(sol.solgrid)