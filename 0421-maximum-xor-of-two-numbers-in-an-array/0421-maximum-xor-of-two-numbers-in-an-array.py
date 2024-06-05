class TriNode:
    def __init__(self):
        self.children=[None]*2
        self.end=True
class Solution:
    def __init__(self):
        self.root=TriNode()
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_ln=len(bin(max(nums)))-2
        def insert(num):
            cur=self.root
            df=max_ln-num.bit_length()
            num=num>>df
            bin_=bin(num)
            for i in bin_[2:]:
                if not cur.children[int(i)]:
                    cur.children[int(i)]=TriNode()
                cur=cur.children[int(i)]
        
        def search(num):
            res=""
            cur=self.root
            bin_=bin(num)
            df=max_ln-len(bin_)+2
            
            # print(len(bin_),num.bit_length())
            bin_=bin_[:2]+'0'*df+bin_[2:]            
            for i in bin_[2:]:
                op=1-int(i)
                if not cur:
                    break
                if cur.children[op]:
                    cur=cur.children[op]
                    res+="1"
                else:
                    cur=cur.children[int(i)]
                    res+="0"
            # print(res,bin_,int("0b"+res,2))
            return int("0b"+res,2)
        
        for i in nums:
            insert(i)
        max_=0
        for i in nums:
            max_=max(max_,search(i))
        return max_
            
