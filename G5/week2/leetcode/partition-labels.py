class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index={}
        for i in range(len(s)):
            last_index[s[i]]=i
        arr=[]
        # print(last_index)
        max_=last_index[s[0]]
        for j in range(len(s)):
            max_=max(last_index[s[j]],max_)
            if j==max_:
                if len(arr)==0:
                    arr.append(max_+1)
                else:
                    arr.append(max_-sum(arr)+1)
            
            
        return arr
            