class Solution:
    import collections, heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # integer array nums, and k
        # k = 5, find top 5 most frequent elements in the array

        # use a heap or not

        priorityQ = []

        freqMap = collections.Counter(nums)

        for number, freq in freqMap.items():
            heapq.heappush(priorityQ, [-freq, number])
            
        res = []
        for i in range(k):
            res.append(heapq.heappop(priorityQ)[1])

        return res
        