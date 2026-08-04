class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # iterate through numbers
        # find target sum

        targetMap = {}
        numToIndex = {}

        for i in range(len(nums)):
            numToIndex[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numToIndex.keys():
                return [i, numToIndex[complement]]

        

        

        # need four's current index
        # realize four's complement was seen
        # retrieve said complement's index