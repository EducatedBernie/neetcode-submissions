class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        boxSets = [[set() for _ in range(3)] for _ in range(3)]


        for row in range(len(board)):
            for col in range(len(board[0])):
                ele = board[row][col]
                if ele != ".":
                    if ele in colSet[col] or ele in rowSet[row] or ele in boxSets[row//3][col//3]:
                        return False
                colSet[col].add(ele)
                rowSet[row].add(ele)
                boxSets[row//3][col//3].add(ele)

        return True    