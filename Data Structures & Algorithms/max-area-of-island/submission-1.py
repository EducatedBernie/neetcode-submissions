class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        seen = set() #set of tuples of coordinates

        numRows = len(grid)
        numCols = len(grid[0])

        
        maxIslandSize = 0
        
        def dfs(row, col):

            if row >= numRows or col >= numCols or row < 0 or col <0:
                return 0
            if (row, col) in seen or grid[row][col] == 0:
                return 0
            else:
                seen.add((row, col))
                
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
                
                
                

        # call dfs on every single ement

        for row in range(numRows):
            for col in range(numCols):
                if (row, col) not in seen:
                    
                    maxIslandSize = max(dfs(row, col), maxIslandSize)

        return maxIslandSize

                
                
            