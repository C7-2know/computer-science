class Solution:
    def smallestNumber(self, num: int) -> int:
        lis=[]
        neg=''
        if num<0:
            neg='-'
        num=abs(num)
        if num==0:
            lis.append(0)
        while num>0:
            n=num%10
            lis.append(n)
            num=num//10
        # print(lis)
        if neg!='':
            lis.sort(reverse=True) 
        else:
            lis.sort() 
        # for i in range
        ind=0
        # if lis[0]=='-':
        #     ind=1
        for i in range(ind,len(lis)):
            if lis[i]!=0:
                lis[ind],lis[i]=lis[i],lis[ind]
                break
        n=''.join(str(i) for i in lis)
        # n=
        print(n)
        # n=
        # print(num)
        n=int(n)
        if neg!='':
            n=0-n
        return n


