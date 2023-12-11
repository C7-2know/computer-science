class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        inc_arr=set()
        inc_set=set([i for i in range(left,right+1)])
        for i in range(len(ranges)):
            inc_arr.update([i for i in range(ranges[i][0],ranges[i][1]+1)])
        return inc_set<=inc_arr
        
