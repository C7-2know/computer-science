class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        def valid(r,c):
            return r<m and r>=0 and c<n and c>=0
        arr=[[float('inf') for _ in range(n)] for _ in range(m)]
        # arr.append(matrix[-1])
        arr[0]=matrix[0]
        print(arr)
        for i in range(m):
            for j in range(n):
                # print(matrix[i][j],matrix[i-1][j],matrix[i][j],matrix[i-1][j-1], matrix[i][j],matrix[i-1][j+1])
                min_=float('inf')
                if valid(i-1,j):
                    arr[i][j]=min(matrix[i][j]+arr[i-1][j],arr[i][j])
                    # print('top',matrix[i][j]+arr[i-1][j],arr[i][j])
                if valid(i-1,j-1):
                    arr[i][j]=min(matrix[i][j]+arr[i-1][j-1],arr[i][j])
                    # print('left',arr[i][j])
                if valid(i-1,j+1):
                    arr[i][j]=min(arr[i][j], matrix[i][j]+arr[i-1][j+1])
                  
        return min(arr[-1])
        # for i in range(m-2,-1,-1):
        #     for j in range(n-1,-1,-1):
        #         min_=float('inf')
        #         if valid(i+1,j-1):
        #             min_=min(min_,arr[i+1][j-1]+matrix[i][j])
        #         if valid(i+1,j+2):
        #             min_=min(min_,arr[i+1][j]+matrix[i][j])
        #         if valid(i+1,j+1):
        #             min_=min(min_,arr[i+1][j+1]+matrix[i][j])
        #         arr[i-1][j]=min_
        #         print(arr)
        # print(arr)
        # return min(arr[0])
                    
        