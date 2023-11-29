class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=0
        x2=x
        while x2>0:
            num=num+x2%10
            num=num*10
            x2=x2//10
        num=num//10
        print(num)
        if num==x:
            return True 
        else:
            return False
        # x=str(x)
        # i=0
        # j=len(x)-1
        # while i<j:
        #     if x[i]!=x[j]:
        #         return False
        #     i+=1
        #     j-=1
        # return True

