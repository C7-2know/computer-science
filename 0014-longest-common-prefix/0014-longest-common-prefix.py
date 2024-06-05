class TriNode:
    def __init__(self):
        self.children=[None]*26
        self.is_end=False
        self.childs=0
class Solution:
    def __init__(self):
        self.root=TriNode()
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # prefix1=''
        # word=''
        # letter=float("inf")
        # for i in strs:
        #     letter=min(letter,len(i))
        #     word=i
        # for i in range(letter):
        #     for j in strs:
        #         if word[i]!= j[i]:
        #             return prefix1
        #     else:
        #         prefix1+=word[i]
        # return prefix1

        def insert(w):
            cur=self.root
            for i in w:
                ind=ord(i)-ord('a')
                if not cur.children[ind]:
                    cur.children[ind]=TriNode()
                cur=cur.children[ind]
                cur.childs+=1
            cur.is_end=True
        
        def search():
            res=''
            cur=self.root
            word=strs[0]
            for i in word:
                ind=ord(i)-ord('a')
                if cur.children[ind] and cur.children[ind].childs<len(strs):
                    return res
                print(cur.childs,i)
                cur=cur.children[ind]
                res+=i
            return res
        for i in strs:
            insert(i)
        return search()
            


                   