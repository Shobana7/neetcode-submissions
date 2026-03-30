class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_left , max_right = 0,0
        max_water = 0

        while l < r:
            if height[l]<=height[r]:
                water = max_left - height[l]
                if water > 0:
                    max_water += water
                max_left = max(max_left, height[l])
                l += 1
            else:
                
                water = max_right - height[r]
                if water > 0:
                    max_water += water
                max_right = max(max_right, height[r])
                r-=1
        
        return max_water