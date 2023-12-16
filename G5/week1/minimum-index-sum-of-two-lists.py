class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        match=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    if len(match)==0:
                        match.append([i,j])
                    elif i+j==sum(match[0]):
                        match.append([i,j])
                    elif i+j<sum(match[0]):
                        match=[[i,j]]
                    break
                    
        out=[]
        for i in range(len(match)):
            out.append(list1[match[i][0]])
        return out