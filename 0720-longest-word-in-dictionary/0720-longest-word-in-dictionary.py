class TriNode:
    def __init__(self):
        self.children=[None for _ in range(26)]
        self.is_end=False
class Solution:
    def __init__(self):
        self.root=TriNode()
    def longestWord(self, words: List[str]) -> str:
        def insert(st):
            cur=self.root
            for i in st:
                ind=ord(i)-ord('a')
                if cur.children[ind]==None:
                    cur.children[ind]=TriNode()
                cur=cur.children[ind]
            cur.is_end=True

        def search(cur=None,max_="",res=[]):
            if cur==None:
                cur=self.root
            if not cur:
                return max_,res
            for i in range(26):
                inp=max_
                if cur.children[i] and cur.children[i].is_end:
                    val,temp=search(cur.children[i],max_+chr(i+ord('a')),res)
                    if len(val)>len(inp):
                        inp=val
            if len(inp)>len(max_):
                max_=inp

            res.append(max_)
            return max_,res
        
        words.sort(key=lambda x:len(x))
        for i in words:
            insert(i)
        val,arr=search()
        arr.sort(key=lambda x:len(x),reverse=True)
        ans=[]
        for i in arr:
            if len(i)==len(arr[0]):
                ans.append(i)
            else:
                break
        ans.sort()
        print(ans)
        return ans[0]