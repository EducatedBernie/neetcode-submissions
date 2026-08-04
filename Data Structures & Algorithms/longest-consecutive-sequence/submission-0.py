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
        maxStreak = 1
        for startingNum in begins:
            currStreak = 1
            currNum = startingNum + 1
            while currNum in seq: # 3
                currNum = currNum + 1 #4
                currStreak += 1 
                maxStreak = max(maxStreak, currStreak)

        

        return maxStreak + 1
            
                
