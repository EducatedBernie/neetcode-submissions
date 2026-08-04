class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        # choices: any number in the list 
        # constraints: can't choose the same number twice that's in path
        # base case: if we're at leaf 
        # what to undo: latest number

        def dfs(index):
            
            if index >= len(nums):
                return

            # base case

            # for choice in choices
            # if choice not constrained:
            # make choice
            # undo choice
