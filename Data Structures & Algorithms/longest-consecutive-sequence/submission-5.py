class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # go through the list

        # mark all the possible beginnings and we check those

        # store everything in a hashmap, O(1) look ups.

        # has one number following it

        

        numSet = set(nums)
        begins = set() # 
        seq = set() #

        for num in nums:
            
            if (num + 1) not in numSet and (num - 1) not in numSet:
                print("eliminated", num)
                continue
            elif (num - 1) not in numSet and ((num + 1) in numSet):
                print("beginning added", num)
                begins.add(num)
            elif (num + 1) in numSet:
                print("seq added", num)
                seq.add(num)
            

        print(begins)
        print(seq)

        # iterate all possible beginnings

        maxStreak = 0
        for startingNum in begins:
            currNum = startingNum + 1
            currStreak = 1
            while currNum in numSet: # 4
                currStreak += 1 # 
                print(currNum)
                
                currNum = currNum + 1 #4
            maxStreak = max(maxStreak, currStreak)

        if numSet == 1:
            return 1
    
        return maxStreak
            
                
