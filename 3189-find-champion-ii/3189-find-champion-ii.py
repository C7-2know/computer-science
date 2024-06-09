class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        stronger=[0 for i in range(n)]
        for i in range(len(edges)):
            stronger[edges[i][1]]+=1
        found=''
        for i in range(len(stronger)):
            if found!='' and stronger[i]==0:
                return -1
            elif stronger[i]==0:
                found=i
        return found if found!='' else -1