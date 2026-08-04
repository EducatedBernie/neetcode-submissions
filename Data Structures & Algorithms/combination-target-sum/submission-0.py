class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        # decision space doesn't diminish 

        # return false when sum exceeds target

        # 

        '''

        def backtrack(path, choices):
            if is_solution(path):
            result.append(path[:])  # save a copy
            return
        
        for choice in choices:
            if is_valid(choice):
                path.append(choice)          # choose
                backtrack(path, remaining)    # explore
                path.pop()                   # un-choose
            
        '''

        # slow way

        # 1, 2 ,3 target = 4

        # choose 1, choose 1, choose 1, choose 1 (valid result add) and return, choose 1 exceed return 



        # choose 1, 2, 1, 
        # choose 1, 2, 2 exceed





        # choose 2

        # map 

        # number of elements: set = {freqMap(string): 000, 010, 111, 0000000001}

        # number of len== 1 paths : {000000001, 000} string where each digit 
        # 2: {}

        # 1 , {10} -> 2 {11}
        # 2, {01} 

        # 0000000000
        # 

        lenToSeenMapping = defaultdict(set)

        


        def backtrack(path, choices): # 1, [1,2,3]
            lst = [0] * 30
            for num in path:
                lst[num - 1] += 1 
            signature = str(lst)

            if signature in lenToSeenMapping[len(path)]:
                return
            lenToSeenMapping[len(path)].add(signature)

            if sum(path) == target:
                res.append(path[:])
                return
            elif sum(path) > target:
                return
            elif sum(path) < target: # 1, [1,2,3]
                for choice in choices:
                    path.append(choice)
                    backtrack(path, choices)
                    path.pop()
                     # new decision time, 1,2, 1,3, 1,1,
            return

        res = []
        path = []

        for num in nums: # choose 1,
            backtrack(path, nums) # just start


        return res
            

            

        
            


