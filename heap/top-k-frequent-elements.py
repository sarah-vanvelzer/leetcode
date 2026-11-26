# Pattern: count freq, use min-heap to sort only first k elements
#   (beats O(nlogn) from sorting all elements)
# Time: O(nlogk)
# Space: O(n) (freq dict)
# Revisit: yes

from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Inputs: list of integers & integer k
        # Outputs: list size k of most frequently occuring ints

        # start by coutning frequencies (using default dict)
        freq = defaultdict(int)

        for i in range(len(nums)):
            freq[nums[i]] += 1
        
        # want to sort only the first k elements in dict
        # use a min-oriented PQ
        heap = []

        for key, val in freq.items():
            # if heap doesn't have k elements
            #   or smallest freq is less than current freq
            if len(heap) < k or heap[0][0] < val:
                heapq.heappush(heap, [val, key])
            # if heap exceeds size k, remove smallest frequency
            if len(heap) > k:
                heapq.heappop(heap)
            
        # return only actual elements (vals) from heap
        return [i for _, i in heap]