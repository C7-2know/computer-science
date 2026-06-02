class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        land_end=sorted(zip(landStartTime, landDuration), key=sum)
        water_end=sorted(zip(waterStartTime, waterDuration),key=sum)
        min_l_end, min_ld= sum(land_end[0]), land_end[0][1]
        min_w_end, min_wd= sum(water_end[0]), water_end[0][1]
        min_=float('inf')
        for st, d in water_end:
            tot=min_l_end+d+(st-min_l_end if st>min_l_end else 0)
            min_=min(tot, min_)
            if st+d>min_:
                break
        for st, d in land_end:
            tot=min_w_end+d+(st-min_w_end if st>min_w_end else 0)
            min_=min(tot, min_)
            if st+d>min_:
                break
        return min_