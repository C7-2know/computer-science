class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
       
        def pop_(arr,num):
            bin_=bin(num)
            ind=len(arr)-1
            for i in range(len(bin_)-1,1,-1):
                if bin_[i]=="1":
                    arr[ind]-=1
                ind-=1
            return arr
        bin_=[0 for i in range(30)]
        for i in nums:
            bin_i=bin(i)
            ind=len(bin_)-1
            for b in range(len(bin_i)-1,1,-1):
                if bin_i[b]=="1":
                    bin_[ind]+=1
                ind-=1
        # print(bin_)
        res=[]
        while nums:
            ind=len(bin_)-1
            k=""
            for j in range(maximumBit):
                # print(bin_[ind])
                if bin_[ind]%2==0:
                    k='1'+k
                else:
                    k='0'+k
                ind-=1
            k="0b"+k
            res.append(int((k),2))
            ls=nums.pop()
            bin_=pop_(bin_,ls)
            # print(bin_,k)

        return res
            
            

        return []
            
        
