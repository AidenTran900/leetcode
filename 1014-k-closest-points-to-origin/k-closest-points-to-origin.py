import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        dist_map = {}
        
        for point in points:
            dist_map[tuple(point)] = sqrt(point[0]**2 + point[1]**2)


        return heapq.nsmallest(
            k,
            points, 
            key=lambda point : dist_map[tuple(point)]
        )