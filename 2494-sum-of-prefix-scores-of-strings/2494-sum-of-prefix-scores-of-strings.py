class TriNode:
    def __init__(self):
        self.children=[None for i in range(26)]
        self.is_end=False
        self.score=0
class Solution:
    def __init__(self):
        self.root=TriNode()
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        def insert(word):
            cur=self.root
            for i in word:
                ind=ord(i)-ord('a')
                if cur.children[ind]==None:
                    cur.children[ind]=TriNode()
                cur.children[ind].score+=1
                cur=cur.children[ind]
            cur.is_end=True
        def search(word):
            cur=self.root 
            count=0
            for i in word:
                ind=ord(i)-ord('a')
                count+=cur.children[ind].score
                cur=cur.children[ind]
            return count
        for i in words:
            insert(i)

        res=[]
        for w in words:
            res.append(search(w))
        return res
