class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dis(x):
            return x[0]**2+x[1]**2
        points.sort(key=dis)
        return points[:k]