class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # most backtracking uses DFS
        # recursive implementation

        res = []

        def dfs(i, subsetSoFar):
            subsetSoFar = subsetSoFar.copy()
            # if i == len(nums) - 1: #base case
            #     res.append(subsetSoFar) #exclude last number 
            #     # subsetSoFar.append(nums[i])
            #     res.append(subsetSoFar) #include last number
            #     return 

            if i == len(nums): #base case
                res.append(subsetSoFar) #exclude last number 
                return 
            

            # recursive part
            dfs(i+1, subsetSoFar) # [1]
            subsetSoFar.append(nums[i])
            dfs(i+1, subsetSoFar) # [1, 2]
    

        dfs(0,[])
        return res
            
  


            
        

      