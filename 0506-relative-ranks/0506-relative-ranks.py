class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dc={score[i]:i for i in range(len(score))}
        res=[0]*len(score)
        score.sort(reverse=True)
        for i in range(len(score)):
            if i==0:
                res[dc[score[i]]]="Gold Medal"
            elif i==1:
                res[dc[score[i]]]="Silver Medal"
            elif i==2:
                res[dc[score[i]]]="Bronze Medal"
            else:
                res[dc[score[i]]]=str(i+1)
        return res

