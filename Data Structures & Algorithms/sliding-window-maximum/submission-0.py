class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        l,r = 0,0
        res = []
        for r in range(k):
            heapq.heappush(maxHeap, (-nums[r],r))
        
        res.append(-maxHeap[0][0])
        r += 1
        while r < len(nums):
            heapq.heappush(maxHeap, (-nums[r],r))
            l += 1

            while maxHeap and l > maxHeap[0][1]:
                heapq.heappop(maxHeap)
            res.append(-maxHeap[0][0])
            r += 1
        
        return res

