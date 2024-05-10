class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        ef_speed=list(zip(efficiency,speed))
        ef_speed.sort(reverse=True)
        max_p=(ef_speed[0][0]*ef_speed[0][1])%(10**9 + 7)
        max_speed=[ef_speed[0][1]]
        sum_=ef_speed[0][1]
        heapify(max_speed)
        ind=1
        # print(max_p,max_speed,ef_speed[0][0])
        for i in range(1,k):
            heappush(max_speed,ef_speed[i][1])
            sum_+=ef_speed[i][1]
            max_p=max(max_p,(sum_*ef_speed[i][0]))
            ind+=1
        while ind<len(ef_speed):
            less=heappop(max_speed)
            if ef_speed[ind][1]<less:
                heappush(max_speed,less)
                ind+=1
                continue
            sum_-=less
            sum_+=ef_speed[ind][1]
            heappush(max_speed,ef_speed[ind][1])
            max_p=max(max_p,(sum_*ef_speed[ind][0]))
            ind+=1
        return max_p%(10**9 + 7)