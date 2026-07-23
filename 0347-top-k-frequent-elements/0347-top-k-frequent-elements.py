class Solution(object):
    def topKFrequent(self, nums, k):
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n,0)
        
        heap = []
        for key in counter.keys():
            heapq.heappush(heap, (counter[key],key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result