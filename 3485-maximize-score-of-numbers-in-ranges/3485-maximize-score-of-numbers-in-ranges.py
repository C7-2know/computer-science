class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        intervals=[[start[i],start[i]+d] for i in range(len(start))]
        def is_pos(num):
            st=intervals[0][0]
            for i in range(1,len(intervals)):
                if st+num>intervals[i][1]:
                    return False
                elif st+num<intervals[i][0]:
                    st=intervals[i][0]
                else:
                    st+=num
            return True

        low=intervals[0][0]
        high=intervals[-1][-1]-low
        low=0
        ans=-1
        while high>=low:
            mid=(high+low)//2
            if is_pos(mid):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans 