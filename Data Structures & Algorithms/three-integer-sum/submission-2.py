class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        end = len(nums)-1

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l,r = i+1, end
            target = -nums[i]

            while l < r:
                numSum = nums[l] + nums[r]
                if numSum == target:
                    res.append([-target, nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1 
                    continue
                if numSum < target:
                    l += 1
                else:
                    r -= 1

        return res