#Approach 1(Using Heap(O(N*logN)N=No of points))
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result_arr=[]
        heapq.heapify(result_arr)
        for point in points:
            distance=((point[1]-0)**2+(point[0]-0)**2)**0.5
            heapq.heappush(result_arr,(distance,point))
        
        ans=[]
        while k!=0:
            point=heapq.heappop(result_arr)
            ans.append(point[1])
            k-=1
        return ans
            
#Approach 2(Using sort):
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p:p[0]**2+p[1]**2)
        return points[:k]