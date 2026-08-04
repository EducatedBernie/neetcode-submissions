class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # input array
        # output true if it contains a value more than once
        # output flase if it doesn't contain a value more than once

        # iter thru the array
            # add elem to a set
            # if already found in set
            # return true

        seen = set()

        for element in nums:
            if element in seen:
                return True
            else:
                seen.add(element)

        return False

        