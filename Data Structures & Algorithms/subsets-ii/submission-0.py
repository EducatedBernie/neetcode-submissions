class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    
        res = set()
        resList = []

        def dfs(i, subsetSoFar):
            subsetSoFar = subsetSoFar.copy()

            if i == len(nums): #base case
                res.add(tuple(subsetSoFar)) #exclude last number 
                return 
            
            # recursive part
            dfs(i+1, subsetSoFar) # [1]
            subsetSoFar.append(nums[i])
            dfs(i+1, subsetSoFar) # [1, 2]
        dfs(0, [])
        
        for tup in res:
            resList.append(list(tup))

        return resList