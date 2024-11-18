class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans=[]
        merged=code+code
        for i in range(len(code)):
            if k>0:
                ans.append(sum(merged[i+1:i+k+1]))
            elif k<0:
                ind=len(code)+i
                ans.append(sum(merged[ind+k:ind]))
            else:
                ans.append(0)
        return ans
