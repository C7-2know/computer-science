class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxx=0
        left=0
        right=len(height)-1
        while left<right:
            area=min(height[left],height[right])*(right-left)
            maxx=max(area,maxx)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxx