class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dc={}
        i=0
        res=[]
        for word in strs:
            tmp=word[:]
            tmp=''.join(sorted(tmp))
            if tmp not in dc:
                dc[tmp]=i
                res.append([])
                i+=1
            res[dc[tmp]].append(word)
        return res
        