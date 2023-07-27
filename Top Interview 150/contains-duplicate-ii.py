from ast import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        setNum = set()
        start = 0
        for i, num in enumerate(nums):
            if num in setNum:
                return True
            setNum.add(num)
            if i >= k:
                setNum.remove(nums[start])
                start += 1
        return False