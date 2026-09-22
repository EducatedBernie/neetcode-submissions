class Solution:
    def trap(self, height: List[int]) -> int:

        
        # computer greaterLeft array
        # compute greaterRight array
            # scan left to right, compute greatest element seen so far going from L to R
            
            # vice versa

        # assert ( as a dry run, all the greater left arrs are correct)

        # compute trapped water
        # scanning each tight

        # water accumulated at position i is given by:
        # min(greaterLeft(i), greaterRight(i)) - height[i]
        # return sum(trappedWater)

        greaterLeft = [0 for _ in range(len(height))]
        greaterRight = [0 for _ in range(len(height))]
        
        for i in range(len(height)): # 0 - len - 1
            if i == 0:
                greaterLeft[i] = 0
            elif i > 0:
                greaterLeft[i] = max(greaterLeft[i - 1], height[i - 1])

        for i in range(len(height) - 1, - 1, -1): # 0 - len - 1
            if i == len(height) - 1:
                greaterRight[i] = 0
            elif i < len(height ) - 1:
                greaterRight[i] = max(greaterRight[i + 1], height[i + 1])

        trappedWater = [0 for _ in range(len(height))]
        for i in range(len(height)):
            trappedWater[i] = max(0, min(greaterLeft[i], greaterRight[i]) - height[i])
        
        return sum(trappedWater)
        
        
        
        

        