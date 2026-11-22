# Pattern: use counter to obtain k most common elements
# Time: O(n)
# Space: O(n)
# Mistakes: only collecting most frequent from Counter instead of all at once
# Revisit: yes

from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Inputs: list of numbers, integer k
        # Outputs: size k list of most frequent numbers

        # Counter uses nlogn
        return [num for num, _ in Counter(nums).most_common(k)]
