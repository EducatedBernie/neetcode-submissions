class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # optimal solution
        # two nums
        # integer target
        # return two indices of addends s.t. they get us target

        # standard solve is N^2

        targetArr = [target - x for x in nums]

        numsIndexMap = {}

        # populate the target map
        for i in range(len(nums)):
            numsIndexMap[nums[i]] = i

        for i in range(len(nums)):
            if targetArr[i] in numsIndexMap:
                j = numsIndexMap[targetArr[i]] #
                if i != j:
                    return [i, j]
            
