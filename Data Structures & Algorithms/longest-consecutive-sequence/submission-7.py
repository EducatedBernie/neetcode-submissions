class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # input - nums
        # output: length of longest conseq sequence that can be formed

        # 

        # a number can either be:
        # 1. start [nothing before, something after]
        # 2. middle [smth before, smth after]
        # 3. end [smth before, nothing after]

        # psuedocode: 

        # loop 
        # add everything into a hashet. 
        # iterate through, decide if something is a start, add it to a set of starts
        # find the next, and the next.

        # find the next start, find the next and the next. 

        if not nums:
            return 0

        # nums = [2, 20, 3, 4, 21, 5, 25]
        # answer is 2,3,4,5

        theSet = set()
        starts = set()
        for number in nums:
            theSet.add(number)

        for number in theSet:
            if number - 1 in theSet:
                continue
            elif number + 1 in theSet:
                starts.add(number)

        # assert(starts == {2, 20})

        longest = 1
        for start in starts: # 2 
            currRun = 1
            while start + 1 in theSet: # 3, 4, 5, 
                start = start + 1
                currRun += 1 #2, 3, 4
            longest = max(longest, currRun)
                
        # assert(longest == 4)
        return longest
