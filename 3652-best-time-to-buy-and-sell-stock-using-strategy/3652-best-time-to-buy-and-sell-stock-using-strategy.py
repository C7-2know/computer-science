class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        pref = [0]
        for i in prices:
            pref.append(i+pref[-1])
        org_profit = [i*j for i,j in zip(prices, strategy)]
        org_pref = [0]
        for i in org_profit:
            org_pref.append(org_pref[-1]+i)
        
        sum_= sum(org_profit)
        st, ls = 1, k
        max_= sum_
        while ls < len(pref):
            wind = org_pref[ls]- org_pref[st-1]
            replace = pref[ls]-pref[st+k//2-1]
            max_ = max(sum_ - wind + replace, max_)
            ls+=1
            st+=1

        return max_
        