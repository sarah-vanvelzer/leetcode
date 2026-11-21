# Time: O(n)
# Space: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Inputs: list of integers & target integer
        # Outputs: list of two indices that add up to target
        # Key = value from list & value = index
        hashmap = {}
        for i in range(len(nums)):
            # Check if value already in hashmap
            if target - nums[i] in hashmap:
                return [i, hashmap[target - nums[i]]]
            # Update hashmap to include current value
            hashmap[nums[i]] = i