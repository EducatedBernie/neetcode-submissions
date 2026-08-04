class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        import math
        # if one pile
        # k = pile [i] // h + 1


        # generally: 
        # h * k >= sum of all K

        # k <=  total bananas / hours 
        # k >= max(piles)

        

        # lots of time, little piles
        # minimum k 

        # big pile, little time
        # maximum k (when h == len(k))

        
        # 

        



        def verify(k, h):
            print("verify ", k)
            for i in range(len(piles)):
                bananasHere = piles[i]
                print("We have", bananasHere, "bananas")
                if k >= bananasHere:
                    bananasHere = 0
                    h -= 1
                    print("ate whole pile one bite")
                    print("h = ", h)
                while bananasHere> 0:
                    bananasHere = bananasHere - k
                    h -= 1
                    print("eat again")
                    print("h = ", h)
            return h

        upper = max(piles) 
        lower = math.ceil(sum(piles)/h)
        print(upper)
        print(lower)
        

        mid = upper + lower // 2
        
        # confirmation equation?

        # search left

        # search right

        '''

        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] >= target:
                r = m
            elif nums[m] < target:
                l = m + 1
        return l if (l < len(nums) and nums[l] == target) else -1
        '''

        # optimalK = -1
        # while lower <= upper:
        #     mid = (upper + lower)// 2
        #     if verify(mid, h) == 0:
        #         optimalK = mid
        #         break
        #     elif verify(mid, h) > 0: #went too fast
        #         upper = mid - 1
        #     else:
        #         lower = mid + 1

        while lower < upper:
            mid = lower + ((upper - lower) // 2)
            if verify(mid, h) >= 0:
                upper = mid
            elif verify(mid, h) < 0:
                lower = mid + 1
        return lower
            

        

            # if h is positive, means K is too high
            # we still have hours remaining

            # if h is 0 it means we're good

            # if h is negative, means K is too low
            # we need more hours than we do. 

        return optimalK
                

