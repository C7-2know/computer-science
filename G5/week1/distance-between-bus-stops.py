class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        min_dis=0
        if start<destination:
            dis1=sum(distance[start:destination])
            dis2=sum(distance[destination:]+distance[:start])
            min_dis=min(dis1,dis2)
        elif start==destination:
            return 0
        else:
            dis1=sum(distance[:destination]+distance[start:])
            dis2=sum(distance[destination:start])
            min_dis=min(dis1,dis2)
            print(distance[:destination]+distance[start:])
        return min_dis