# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # how to determine a singular good node.

        # start from the node traverse up?

        # root is usually good

        # bfs, something about strictly increasing stuff 

        # 2,  1 , 3 , 1 , 5

        numGood = 0

        def dfs(node, maxPathNumber):
            nonlocal numGood
            if not node:
                return False

            if node.val >= maxPathNumber:
                numGood += 1

            maxPathNumber = max(maxPathNumber, node.val)

            dfs(node.left, maxPathNumber)
            dfs(node.right, maxPathNumber)

        dfs(root, maxPathNumber=root.val)

        return numGood