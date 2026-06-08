class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        def present_in_left_half(left, right, num):
            if nums[right] < nums[mid]:
                if nums[left] <= target <= nums[num]:
                    return True
                return False
            else:
                if nums[mid] < target <= nums[right]:
                    return False
                return True

        while l < r:
            mid = l + (r-l)//2

            if present_in_left_half(l,r,mid):
                r = mid
            else:
                l = mid + 1
        
        if nums[l] == target:
            return l
        return -1
