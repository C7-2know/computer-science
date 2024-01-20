class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        wind={}
        max_=0
        left=0
        right=0
        chg=0
        while right<len(answerKey):
            if right==0:
                wind['T']=0
                wind['F']=0
            wind[answerKey[right]]+=1
            min_=min(wind.values())
            while min_>k:
                wind[answerKey[left]]-=1
                min_=min(wind.values())
                left+=1
            max_=max(max_,sum(wind.values()))
            right+=1
        return max_


