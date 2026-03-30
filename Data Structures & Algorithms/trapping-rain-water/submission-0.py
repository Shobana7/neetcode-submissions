class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_left , max_right = 0,0
        max_water = 0

        while l < r:
            if height[l]<=height[r]:
                max_left = max(max_left, height[l])
                water = max_left - height[l]
                if water > 0:
                    max_water += water
                l += 1
            else:
                max_right = max(max_right, height[r])
                water = max_right - height[r]
                if water > 0:
                    max_water += water
                r-=1
        
        return max_water