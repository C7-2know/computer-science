class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPali(st):
            ln=len(st)
            if ln==1:
                return True
            if ln%2==0:
                return st[:ln//2]==st[ln//2:][::-1]
            # print(st[ln//2+1:][::-1])
            return st[:ln//2]==st[ln//2+1:][::-1]
        # print("return",isPali('abba'))
        res=[]
        def back(i,word,curr):
            if word=="":
                res.append(curr[:])
            # print('word',word)
            for ind in range(len(word)):
                # print(word[:ind+1])
                # print(word[:ind+1],isPali(word[:ind+1]),curr)
                if isPali(word[:ind+1]):
                    curr.append(word[:ind+1])
                    back(ind+1,word[ind+1:],curr)
                    curr.pop()
                # word+=s[ind]

        back(0,s,[])
        return res

        # def dp(i,st):
        #     if i>=len(s):
        #         return []
        #     if st:
        #         return dp(i+1,st+s[i]).append([st])
        #     else:
        #         return dp(i+1,st+s[i])
        # return dp(0,'')

                