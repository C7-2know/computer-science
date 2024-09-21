class Trie:
    def __init__(self,num):
        self.children=[None for _ in range(10)]
        self.val=num
        self.is_end=True
    def insert(self,num,turn):
        if turn<0:
            return
        cur=self 
        st=0  
        if cur.val=="":
            st=1         
        for i in range(st,10):
            if int(cur.val+str(i))<=num:
                cur.children[i]=Trie(cur.val+str(i))
                cur.children[i].insert(num,turn-1)
            
    def search(self):
        if self==None:
            return []
        cur=self
        ans=[]
        if cur.val!="":
            ans.append(int(cur.val))
        for i in range(10):
            if cur.children[i]!=None:
                res=cur.children[i].search()
                ans+=res
        return ans

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        trie=Trie("")
        trie.insert(n,n//10+1)
        return trie.search()

                    
        