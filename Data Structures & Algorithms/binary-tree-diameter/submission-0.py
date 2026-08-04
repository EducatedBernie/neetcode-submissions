# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        globMax = 0

        # at every step in the algo update global max
        def diameter(root):
            nonlocal globMax

            if not root:
                return

            dia = howtall(root.left, 0) + howtall(root.right, 0)
            globMax = max(dia, globMax)
            
            diameter(root.left)
            diameter(root.right)

            return
        

        def howtall(root, h):
            if not root:
                return h
            return max(howtall(root.left, h+1), howtall(root.right, h+1))
        
        diameter(root)

        return globMax

