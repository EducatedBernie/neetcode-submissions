# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        def bfs(node):
            if not node:
                return []

            q = deque()
            q.append(node)
            res = []

            

            while q:
                level = []
                for i in range(len(q)):
                    curr = q.popleft()
                    level.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                    
                res.append(level)

            return res
        return bfs(root)
                


                

                