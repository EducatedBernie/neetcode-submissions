class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return None

         # input: an array [] and k
         # return top 5 most frequent elements


        # k = 3
        # nums = [1, 2, 3, 3, 4, 4, 5, 5]
        # nums = [1]

        # 1, freq 3
        # 2, freq 1
        # 3 freq 2 

        buckets = [[] for _ in range(len(nums))] # 1

        ctr = collections.Counter(nums)

        for num, freq in ctr.items():
            buckets[freq-1].append(num)

        # assert(3 in buckets[2] and 5 in buckets[2] and 4 in buckets[2])

        ans = []
        for i in range(len(nums) - 1, -1, -1): # 8 times
            if buckets[i]:
                ans.extend(buckets[i])
            if len(ans) == k:
                # print(ans)
                # assert(3 in ans and 5 in ans and 4 in ans)
                return ans
            else:
                continue