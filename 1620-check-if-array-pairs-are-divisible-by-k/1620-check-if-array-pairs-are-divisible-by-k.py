class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n_dc={}
        p_dc={}
        for i in range(len(arr)):
            if arr[i]>=0:
                if arr[i]%k not in p_dc:
                    p_dc[arr[i]%k]=set()
                p_dc[arr[i]%k].add(i)
            else:
                if arr[i]%k not in n_dc:
                    n_dc[arr[i]%k]=set()
                n_dc[arr[i]%k].add(i)
        count=0
        visited=set()
        for j in range(len(arr)):
            if j in visited:
                continue
            else:
                indx=-1
                if arr[j]<0:
                    n_dc[arr[j]%k].remove(j)
                    if len(n_dc[arr[j]%k])==0:
                        n_dc.pop(arr[j]%k)
                else:
                    p_dc[arr[j]%k].remove(j)
                    if len(p_dc[arr[j]%k])==0:
                        p_dc.pop(arr[j]%k)
                visited.add(j)
                
                p2=(-arr[j])%k
                if p2 in p_dc:
                    count+=1
                    indx=p_dc[p2].pop()
                    visited.add(indx)
                    if len(p_dc[p2])==0:
                        p_dc.pop(p2) 
                elif p2 in n_dc:
                    count+=1
                    indx=n_dc[p2].pop()
                    visited.add(indx)
                    if len(n_dc[p2])==0:
                        n_dc.pop(p2)
        return count==len(arr)/2