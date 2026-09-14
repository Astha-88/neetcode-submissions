class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consec = set(nums)
        longest = 0

        for i in consec:
            if i - 1 not in consec:
                length = 0
                while i + length in consec:
                    length += 1

                longest = max(longest,length)

        return longest