class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # go through the list

        # mark all the possible beginnings and we check those

        # store everything in a hashmap, O(1) look ups.

        # has one number following it

        numSet = set(nums)
        begins = set() # 
        seq = set() #

        if len(nums) == 1:
            return 1


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
            currNum = startingNum
            currStreak = 0
            while currNum in numSet: # 4
                currStreak += 1 # 
                print(currNum)
                maxStreak = max(maxStreak, currStreak)
                currNum = currNum + 1 #4

        

        return maxStreak
            
                
