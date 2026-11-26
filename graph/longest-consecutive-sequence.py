# Pattern: only count if start of sequence (avoids O(n^2))
# Time: O(n)
# Space: O(n)
# Mistakes: recognition
# Revisit: yes

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Inputs: list of nums
        # Outputs: size of longest consecutive elements

        # put all nums in a set
        s = set(nums)
        longest = 0

        for num in s:
            # only count if start of sequence
            length = 1
            if num - 1 not in s:
                while num + 1 in s:
                    length += 1
                    num += 1
                longest = max(longest, length)
        
        return longest