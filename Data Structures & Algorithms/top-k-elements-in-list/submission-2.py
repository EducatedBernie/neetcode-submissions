class Solution:
    from collections import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ctr = collections.Counter(nums)
        
            

        hp = []
        numElements = 0
        heapq.heapify(hp)

        for number, freq in ctr.items():
            heapq.heappush(hp, (freq, number))
            if numElements == k:
                heapq.heappop(hp)
                numElements -= 1
            numElements += 1

        res = []
        for tup in hp:
            res.append(tup[1])
        

        return res
        