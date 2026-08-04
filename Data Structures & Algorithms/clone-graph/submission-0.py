"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # use dfs to traverse 
        # keep a map of clone

        if not node:
            return

        cloneMap = {}
        
        visited = set()


        def dfs(node):
            if not node:
                return 
            if node in visited:
                return
            visited.add(node)
            if node.val not in cloneMap.keys(): #clone ourselves if not cloned already
                # can we also dupe neighbors here.
                cloneMap[node.val] = Node(node.val, [])
                # dupe neighbours in a loop
                # check current neighbours and clone them
                # add cloned neighbours to cloned node
            for nei in node.neighbors:
                if nei.val not in cloneMap.keys():
                    cloneMap[nei.val] = Node(nei.val)
                cloneMap[node.val].neighbors.append(cloneMap[nei.val])
                dfs(nei)

        dfs(node)
        return cloneMap[node.val]