class Solution:
    def minOperations(self, s: str) -> int:
        op1, op2= 0,0
        one,zero='1', '0'
        for i in s:
            if i!=one:
                op1+=1
            if i!=zero:
                op2+=1
            one, zero=zero,one
        return min(op1, op2)