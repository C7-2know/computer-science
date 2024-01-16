class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
       

        mid=len(cardPoints)-k
        wind_sum=sum(cardPoints[:mid])
        total=sum(cardPoints)
        max_s=total-wind_sum
        for i in range(mid,len(cardPoints)):
            # print(wind_sum,max_s)
            wind_sum=wind_sum-cardPoints[i-mid]+cardPoints[i]
            max_s=max(total-wind_sum,max_s)
        return max_s
