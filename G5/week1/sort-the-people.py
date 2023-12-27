class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # using Buble sort
        # for i in range(len(names)):
        #     act=False
        #     for j in range(1,len(heights)):
        #         if heights[j]>heights[j-1]:
        #             heights[j],heights[j-1]=heights[j-1],heights[j]
        #             names[j],names[j-1]=names[j-1],names[j]
        #             act=True
        # return names

        # using selection sort
        # for i in range(len(heights)):
        #     for j in range(i+1,len(heights)):
        #         if heights[j]>heights[i]:
        #             heights[i],heights[j]=heights[j],heights[i]
        #             names[i],names[j]=names[j],names[i]       
        # return names

        # using counting sort
        # dc={}
        # for i in range(len(heights)):
        #     dc[heights[i]]=i
        
        # mi=min(heights)
        # ma=max(heights)
        # arr=[0 for i in range(mi,ma+1)]
        # for j in heights:
        #     arr[j-mi]+=1
        # out=[]
        # for k in range(len(arr)-1,-1,-1):
        #     for j in range(arr[k]):
        #         print(mi+k, dc[mi+k],arr[k])
        #         indx=dc[mi+k]
        #         out.append(names[indx])
        # return out


        zipped=list(zip(heights,names))
        zipped.sort(key=lambda a:a[0], reverse=True)
        names=[n for _, n in zipped]
        return names
        

            