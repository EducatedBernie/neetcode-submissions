# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        def dfs(node):
            if not node:
                return node
            
            # at ancestor
            if node.val == p.val or node.val == q.val:
                return node

            # at split point

            if (node.val > p.val and node.val < q.val ) or (node.val < p.val and node.val > q.val):
                return node

            # go right
            
            if p.val > node.val and q.val > node.val:
                return dfs(node.right)

            # keep going left

            elif p.val < node.val and q.val < node.val:
                return dfs(node.left)

        return dfs(root)

           
