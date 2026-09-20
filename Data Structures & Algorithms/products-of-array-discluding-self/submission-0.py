class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Input: nums = [1,2,4,6]

        [1,2,4,6]
        [48,24,,6]
        
        
        
        
        '''

        leftToRight = [0] * len(nums)
        rightToLeft = [0] * len(nums)

        # leftToRight
        for i in range(len(nums)):
            if i == 0:
                leftToRight[i] = nums[i]
            else:
                leftToRight[i] = nums[i] * leftToRight[i-1]

        # assert(leftToRight == [2, 4, 8, 16 ,32])

        #rightToLeft

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                rightToLeft[i] = nums[i]
            else:
                rightToLeft[i] = nums[i] * rightToLeft[i+1]

        # assert(rightToLeft == [32, 16, 8, 4, 2])

        ans = [0] * len(nums)

        ans[0] = rightToLeft[1]
        # assert(ans[0] == 16)
        ans[-1] = leftToRight[-2]
        # assert(ans[-1] == 16)
        for i in range(1, len(nums)-1):
            ans[i] = leftToRight[i-1] * rightToLeft[i + 1]

        return ans
        