# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        arr1 = []
        arr2 = []

        def bfs(root, arr):
            q = deque()
            q.append(root)

            while q:
                for i in range(len(q)):
                    curr = q.popleft()
                    if curr != None:
                        arr.append(curr.val)
                        if curr.left:
                            q.append(curr.left)
                        else:
                            q.append(None)
                        if curr.right:
                            q.append(curr.right)
                        else:
                            q.append(None)

                    else:
                        arr.append(None)
                    

            return arr

        return bfs(p,arr1) == bfs(q,arr2)
