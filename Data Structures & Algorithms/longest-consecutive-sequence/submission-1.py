class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        unique = set(nums)
        maxLen = 0

        for i in unique:
            if i-1 in unique:
                continue
            length_so_far = 1

            while i + length_so_far in unique:
                length_so_far += 1

            maxLen = max(maxLen, length_so_far)
        
        return maxLen


