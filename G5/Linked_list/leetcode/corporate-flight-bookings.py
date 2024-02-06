class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # res=[0 for i in range(n)]
        # for k in range(len(bookings)):
        #     st=bookings[k][0]
        #     end=bookings[k][1]+1
        #     print(math.sum([1,2,3],[1,2,3]))
        #     # res[st:end]+=[bookings[2] for _ in range(st,end)]
        # return res

        arr = [0]*(n+1)
        for lv, ar, seats in bookings:
            arr[lv-1]+= seats
            arr[ar]-= seats

        return list(accumulate(arr[:-1]))


        # ans=[0 for j in range(n)]
        # for i in range(len(bookings)):
        #     for k in range(bookings[i][0],bookings[i][1]+1):
        #         ans[k-1]+=bookings[i][2]
        # return ans


        # ans=[0 for j in range(n)]
        # dc={}
        # for i in range(len(bookings)):
        #     dc[(bookings[i][0],bookings[i][1])]=dc.get((bookings[i][0],bookings[i][1]),0)+bookings[i][2]
        # for z in dc:
        #     a,b=z
        #     for p in range(a,b+1):
        #         ans[p-1]+=dc[z]
        # return ans
            