# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def ht(node, level):
            if not node:
                return level
            
            return 1 + max(ht(node.left, level), ht(node.right, level))

        

        def balance(node, level):
            if not node:
                return True
            return (abs(ht(node.left, level) - ht(node.right, level)) <= 1)

        return balance(root, 0)