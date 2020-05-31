#Approach 1(Optimized Approach in a first Attempt):
class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        #Two Pointer Solution
        index_i=0
        index_j=0
        len_A=len(A)
        len_B=len(B)
        result=[]
        while index_i<len_A and index_j<len_B:
            if A[index_i][0]>B[index_j][0] and A[index_i][0]>B[index_j][1]:
                index_j+=1
            elif B[index_j][0]>A[index_i][0] and B[index_j][0]>A[index_i][1]:
                index_i+=1
            else:
                if A[index_i][1]>=B[index_j][1]:
                    result.append([max(A[index_i][0],B[index_j][0]),B[index_j][1]])
                    index_j+=1
                else:
                    result.append([max(A[index_i][0],B[index_j][0]),A[index_i][1]])
                    index_i+=1
        return result
    
    