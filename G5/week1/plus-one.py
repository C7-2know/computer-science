class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]==9:
            first=0
            for i in range(len(digits)-1,-1,-1):
                if digits[i]+1!=10:
                    digits[i]+=1
                    break
                digits[i]=0
            if digits[0]==0:
                digits.insert(i,1)
        else:
            digits[-1]+=1
        return digits