class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            maxx = max(area, maxx)
            
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return maxx
