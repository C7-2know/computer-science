class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        prefix=[]
        max_=items[0][1]

        for c,b in items:
            max_=max(max_,b)
            prefix.append(max_)
        print(prefix)
        def max_p(q):
            l,r=0,len(items)-1
            while l<=r:
                ans=-1
                mid=(l+r)//2
                if items[mid][0]>q:
                    r=mid-1
                else:
                    l=mid+1
            return l-1 
        ans=[]
        for q in queries:
            ind=max_p(q)
            if ind<0:
                ans.append(0)
            else:
                ans.append(prefix[ind])
        return ans