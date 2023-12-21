class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # new=[]
        # for i in range(len(strs[0])):
        #     w1=strs[:][i]
        #     new.append(w1)
        #     print(new)
        # for j in range(len(new))
        # return 3


        remove=0
        for j in range(len(strs[0])):
            # prev=96
            for i in range(1,len(strs)):
                # print(ord(strs[i][j]))
                if ord(strs[i-1][j])>ord(strs[i][j]):
                    remove+=1
                    break
                # prev=ord(strs[i][j])
        return remove