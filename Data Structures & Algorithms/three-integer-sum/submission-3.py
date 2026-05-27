class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def twoSum(target, arr):
            pairs = set()
            complement = {}

            for n in arr:
                comp = target - n
                if comp in complement:
                    pairs.add((n, comp))
                complement[n] = n

            return pairs

        nums.sort()

        res = []
        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            target = -num
            pairs = twoSum(target, nums[idx+1:len(nums)])

            for x,y in pairs:
                res.append([x,y,num])
        

        return res


