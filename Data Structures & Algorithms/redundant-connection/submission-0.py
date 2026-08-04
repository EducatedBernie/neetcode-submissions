class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # how to remove a cycle by removing one of the edges that has created the cycle.
        # removing any edge within the cycle would work. 

        # make it into a directed graph. 

        # make parent array

        parent = {}

        for u, v in edges:
            parent[u] = u
            parent[v] = v

        def union(a, b):
            parent[find(a)] = find(b)

        def find(a):
            if parent[a] == a:
                return a
            return find(parent[a])

        for u, v in edges:
            if find(u) == find(v):
                return [u, v]
            else:
                union(u,v)