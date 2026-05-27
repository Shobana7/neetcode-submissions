class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maxLen = 0

        for k in freq:
            if k - 1 in freq:
                continue
            length_so_far = 1
            next_elem = k + 1
            while next_elem in freq:
                length_so_far += 1
                next_elem += 1

            maxLen = max(maxLen, length_so_far)

        return maxLen 