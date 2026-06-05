class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        tot=0
        for num in range(max(num1,101),num2+1):
            i=1
            num=str(num)
            while i<len(num)-1:
                if (num[i]<num[i-1] and num[i]<num[i+1]) or (num[i]>num[i-1] and num[i]>num[i+1]):
                    tot+=1
                i+=1
        return tot