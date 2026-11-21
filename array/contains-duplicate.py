# Time: O(n)
# Space: O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Inputs: list of ints
        # Outputs: True if contains duplicate elements, False otherwise
        num_set = set()
        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)
        # No duplicates
        return False