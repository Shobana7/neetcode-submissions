class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l,r = 0, len(heights)-1

        while l < r:
            w = (r-l)
            if heights[l] < heights[r]:
                maxWater = max(maxWater, w* heights[l])
                l += 1
            else:
                maxWater = max(maxWater, w*heights[r])
                r -= 1
        
        return maxWater