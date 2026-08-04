class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        seen = set() #set of tuples of coordinates

        numRows = len(grid)
        numCols = len(grid[0])

        currIslandSize = 0
        maxIslandSize = 0
        
        def dfs(row, col):
            nonlocal currIslandSize
            if row >= numRows or col >= numCols or row < 0 or col <0:
                return
            if (row, col) in seen or grid[row][col] == 0:
                return
            else:
                seen.add((row, col))
                element = grid[row][col]
                if element == 1:
                    # increment size of current island
                    currIslandSize += 1
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)

        # call dfs on every single ement

        for row in range(numRows):
            for col in range(numCols):
                if (row, col) not in seen:
                    currIslandSize = 0
                    dfs(row, col)
                    maxIslandSize = max(currIslandSize, maxIslandSize)

        return maxIslandSize

                
                
            