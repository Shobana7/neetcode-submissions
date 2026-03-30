class Solution:
    def topKFrequent(self, nums: List[int], n: int) -> List[int]:
        count = Counter(nums)

        maxHeap = []

        for k, v in count.items():
            heapq.heappush(maxHeap, (v,k))

        while len(maxHeap) > n:
            heapq.heappop(maxHeap)
        
        return [i for c,i in maxHeap]
