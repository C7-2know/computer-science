class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vouw="aeiou"
        dc={vouw[i]:i+2 for i in range(5)}
        count="0b"+"0"*5
        visited={}
        max_=0
        left=0
        cons=0
        for i in range(len(s)):
            if s[i] in dc:
                ind=dc[s[i]]
                b=abs(int(count[ind])-1)
                count=count[:ind]+str(b)+count[ind+1:]
    
            if int(count,2)!=0:
                if count in visited:
                    max_=max(max_,i-visited[count])
                else:
                    visited[count]=i
            else:
                max_=max(max_,i-left+1)
                
        return max_



