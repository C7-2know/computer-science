class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo={}
        def dp(i,day):
            if i>=len(days):
                return 0
            if days[i]<day:
                return dp(i+1,day)
            if( i,day )not in memo:
                first=dp(i+1,days[i]+1)+costs[0]
                sec=dp(i+1,days[i]+7)+costs[1]
                thid=dp(i+1,days[i]+30)+costs[2]
                # print(first,sec,thid)
                memo[(i,day)]= min(first,sec,thid)
            return memo[(i,day)]
        print(memo)

        return dp(0,1)