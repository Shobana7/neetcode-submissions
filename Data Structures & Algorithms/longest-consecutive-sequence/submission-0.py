class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        unique = Counter(nums)
        maxLen = 0

        for i in unique:
            length_so_far = 1
            nextNum = i + 1
            while nextNum in unique:
                length_so_far += 1
                nextNum += 1
            
            maxLen = max(maxLen, length_so_far)
        
        return maxLen


