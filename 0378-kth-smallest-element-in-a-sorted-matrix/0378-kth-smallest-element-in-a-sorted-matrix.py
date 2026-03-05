class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def find_k(num):
            count=0
            for i in range(len(matrix)):
                left, right=0,len(matrix[0])
                while left<right:
                    mid=left+(right-left)//2
                    if matrix[i][mid]>num:
                        right=mid
                    else:
                        left=mid+1
                count+=left
            return count

        min_, max_=matrix[0][0], matrix[-1][-1]
        while min_<max_:
            mid=min_+(max_-min_)//2
            kth=find_k(mid)
            if kth<k:
                min_=mid+1
            else:
                max_=mid
        return min_