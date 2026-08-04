class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        # calculate the mid row


        lowRow = 0
        highRow = len(matrix) - 1
        lowCol = 0
        highCol = len(matrix[0]) - 1
        targetRow = -1

        while lowRow <= highRow:
            midRow = (lowRow + highRow) // 2
                
            if matrix[midRow][lowCol] <= target and matrix[midRow][highCol] >= target:
                targetRow = midRow
                break
            # if the smallest element is greater than target search lower row
            elif matrix[midRow][lowCol] > target:
                highRow = midRow - 1
            # if the largest element is smaller target search higher row
            elif matrix[midRow][highCol] < target:
                lowRow = midRow + 1
            
        if targetRow == -1:
            return False 

        arr = matrix[targetRow]

        print(targetRow)
        while lowCol <= highCol:
            midCol = (lowCol + highCol) //2
            if arr[midCol] == target:
                return True
            elif arr[midCol] > target:
                highCol = midCol - 1
            else:
                lowCol = midCol + 1
        return False
            # we're cooked. bail 
        # return target
        
        # search the row
        # while 


        
        # calculate the corr element of the row. 

