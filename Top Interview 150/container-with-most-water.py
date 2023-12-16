# first, calculate the area of the container using both extremes
# then, check which value is smaller and slide it one index towards the center

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = -1
        maxArea = 0
        while start < len(height) + end:
            if min(height[start], height[end]) * (len(height) + end - start) > maxArea:
                maxArea = min(height[start], height[end]) * (len(height) + end - start)
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return maxArea
        