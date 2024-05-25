class TriNode:
    def __init__(self):
        self.children=[None for _ in range(26)]
        self.end=False
class Solution:
    def __init__(self):
        self.root=TriNode()
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def insert(word):
            cur=self.root
            for i in word:
                ind=ord(i)-ord('a')
                if cur.children[ind]==None:
                    cur.children[ind]=TriNode()
                cur=cur.children[ind]
            cur.end=True
        def search(word):
            res=''
            cur=self.root
            i=0
            ind=ord(word[i])-ord('a')
            while cur and cur.children[ind]!=None and i<len(word):
                res+=word[i]
                # print(word[:i+1],cur.end)
                i+=1
                cur=cur.children[ind]
                if cur.end:
                    break
                if i<len(word):
                    ind=ord(word[i])-ord('a')
            if res=="" or cur.end==False:
                return word
            return res
        for i in dictionary:
            insert(i)
        words=sentence.split(' ')
        out=''
        for w in words:
            res=search(w)
            out+=res+" "
        return out[:-1]
        