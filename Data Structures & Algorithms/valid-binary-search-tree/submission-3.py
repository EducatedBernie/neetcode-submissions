# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def bfs(node):
            if not node:
                return True

            q = deque()
            q.append((node, None, None))

            while q:
                curr, lessThan, greaterThan = q.popleft()
                print(curr.val, lessThan, greaterThan)
                if (lessThan or lessThan == 0) and not greaterThan:
                    if curr.val >= lessThan:
                        return False

                elif (greaterThan or greaterThan == 0) and not lessThan:
                    if curr.val <= greaterThan:
                        return False
                    
            
                if curr.left:
                    q.append((curr.left, curr.val, None))
                if curr.right:
                    q.append((curr.right, None , curr.val))

            return True

        return bfs(root)
                    
                    
                


                

            

            