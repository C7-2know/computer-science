class Solution:
    def reachNumber(self, target: int) -> int:
        steps=0
        sum_=0
        target=abs(target)
        while sum_<target:
            steps+=1
            sum_+=steps
        print(sum_,steps)
        while (sum_-target)%2!=0:
            steps+=1
            sum_+=steps
        return steps