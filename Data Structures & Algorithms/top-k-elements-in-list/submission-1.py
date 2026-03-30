class Solution:
    def topKFrequent(self, nums: List[int], n: int) -> List[int]:
        count = Counter(nums)

        minHeap = []

        for k, v in count.items():
            heapq.heappush(minHeap, (v,k))

        while len(minHeap) > n:
            heapq.heappop(minHeap)
        
        return [i for c,i in minHeap]
