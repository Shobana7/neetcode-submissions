class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for i in stones:
            heapq.heappush(maxHeap, -i)
        
        while len(maxHeap)>1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)

            if x == y:
                continue
            if x < y:
                heapq.heappush(maxHeap, x-y)
            else:
                heapq.heappush(maxHeap, y-x)
        
        return -maxHeap[0] if len(maxHeap)== 1 else 0