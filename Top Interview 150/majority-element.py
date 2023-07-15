from ast import List
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
            if map[num] > len(nums) / 2:
                return num