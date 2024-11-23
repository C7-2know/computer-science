class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        mat=[]
        for i in range(len(box)):
            row=[]
            stone=0
            for j in range(len(box[0])):
                if box[i][j]=="#":
                    stone+=1
                elif box[i][j]=="*":
                    stone=0
                row.append(stone)
            mat.append(row)
        res=[[] for _ in range(len(box[0]))]
        for i in range(len(box[0])-1,-1,-1):
            for j in range(len(box)-1,-1,-1):
                if mat[j][i]!=0:
                    res[i].append("#")
                    mat[j][i-1]=mat[j][i]-1
                elif mat[j][i]==0 and box[j][i]!="*":
                    res[i].append(".")
                    mat[j][i-1]=0
                elif box[j][i]=="*":
                    res[i].append("*")
                elif box[j][i]!="*" and mat[j][i]>0:
                    res.append["."]
                else:
                    res[i].append(".")
        return res
                

            