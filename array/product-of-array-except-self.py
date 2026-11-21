# Pattern: right & left swipes to get products up until specific index
# Time: O(n)
# Space: O(n)
# Mistakes: recognizing right & left swipes
# Revisit: yes

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Inputs: list of ints
        # Outputs: list of products excluding current index
        # Idea: take product of everything to the left & multiply
        #   by everything to the right

        left = []
        # Init right array so we can fill from back to front
        right = [0] * len(nums)
        answer = []

        # Left swipe
        for i in range(len(nums)):
            if i == 0:
                left.append(nums[i])
            else:
                left.append(nums[i] * left[i-1])
        
        # Right swipe
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                right[i] = nums[i]
            else:
                right[i] = nums[i] * right[i+1]
        
        # Calculate for every index i
        for i in range(len(nums)):
            # First index
            if i == 0:
                answer.append(right[1])
            # Last index
            elif i == len(nums)-1:
                answer.append(left[len(nums)-2])
            else:
                answer.append(left[i-1] * right[i+1])
        
        return answer