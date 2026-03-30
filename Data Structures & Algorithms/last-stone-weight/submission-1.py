class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for i in stones:
            heapq.heappush(maxHeap, -i)
        
        while len(maxHeap)>1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            
            if x < y:
                heapq.heappush(maxHeap, x-y)

        
        return -maxHeap[0] if len(maxHeap)== 1 else 0