class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # c=0
        # for i in range(len(s)-1,-1,-1):
        #     if s[i]==" " and c==0:
        #         continue
        #     elif s[i]==" ":
        #         break
        #     c+=1
        # return c

        s=s.strip().split()
        return len(s[-1])