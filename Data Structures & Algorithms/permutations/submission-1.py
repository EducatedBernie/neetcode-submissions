class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        # choices: any number in the list 
        # constraints: can't choose the same number twice that's in path
        # base case: if we're at leaf 
        # what to undo: latest number


        res = []

        def dfs(index, path):
            
            if index >= len(nums):
                # append copy, return
                res.append(path.copy())
                return

            for num in nums:
                if num not in path:
                    path.append(num)
                    dfs(index + 1, path)
                    path.pop()
            return

        dfs(0, [])
    
        return res
            # base case

            # for choice in choices
            # if choice not constrained:
            # make choice
            # undo choice

        # start dfs
