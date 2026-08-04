# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = 0
        
        def ht(node, level):
            if not node:
                return level

            level += 1

            diameter = ht(node.left, level) + ht(node.right, level)
            maxD = max(maxD, diameter)
            return max(ht(node.left, level), ht(node.right, level))

        return maxD

            

            
            