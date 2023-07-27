# note: this solution is very slow and will be optimized in the future
from ast import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        while i < len(numbers):
            num1 = numbers[i]
            try:
                ind = numbers.index(target - num1, i + 1, len(numbers))
            except ValueError:
                i += 1
            else:
                num2 = numbers[ind]
                return [i + 1, ind + 1]
        return []
