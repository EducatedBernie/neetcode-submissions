# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def ht(node, level):
            if not node:
                return level

            level += 1

            return max(ht(node.left, level), ht(node.right, level))

        return ht(root.left, 0) + ht(root.right, 0)

            

            
            