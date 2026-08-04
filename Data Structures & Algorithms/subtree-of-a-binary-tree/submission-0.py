# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        # new skill, see if the trees are the same using dfs

        def dfs(r1, r2):
            if r1 and not r2:
                return False
            if r2 and not r1:
                return False
            if not r1 and not r2:
                return True
        
            return dfs(r1.left, r2.left) and dfs(r1.right, r2.right) and r1.val == r2.val

        
        def search(node, lf):

            if not node:
                return False
            if node.val == lf:
                return dfs(node, subRoot)
            
            return search(node.left, lf) or search(node.right, lf)

        return search(root, subRoot.val)

            
            