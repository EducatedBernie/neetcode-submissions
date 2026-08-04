class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        '''
        def backtrack(path, choices):
             if is_solution(path):
            result.append(path[:])  # save a copy
        return
    
        for choice in choices:
            if is_valid(choice):
                path.append(choice)          # choose
                backtrack(path, remaining)    # explore
                path.pop()         
            
        '''

        res = []
        res.append([])
        path = []

        def explore(path, remaining):
            if not remaining:
                return
            #include case
            path.append(remaining[0])  #append the decision onto path
            res.append(path[:])  # append subset with inclusion
            explore(path, remaining[1:])
            # exclude case
            path.pop() 
            explore(path, remaining[1:])
            

        explore(path, nums)

        return res

            
