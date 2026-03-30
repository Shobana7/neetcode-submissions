class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        nums.sort()
        end = len(nums)-1

        for i in range(len(nums)):
            target = -nums[i]
            l,r = i+1, end

            while l < r:
                numSum = nums[l] + nums[r]
                if numSum == target:
                    triplet = [-target, nums[l],nums[r]]
                    triplet.sort()
                    res.add(tuple(triplet))
                    l += 1
                    r -= 1
                    continue
                if numSum < target:
                    l += 1
                else:
                    r -= 1

        return list(res)