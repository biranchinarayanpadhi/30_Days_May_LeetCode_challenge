#Recursive Approach(TLE)
class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        len1=len(A)
        len2=len(B)
        return self.LCS(A,B,0,0,len1,len2)
    
    def LCS(self,A,B,i,j,len1,len2):
        if i==len1 or j==len2:
            return 0
        elif A[i]==B[j]:
            return 1+self.LCS(A,B,i+1,j+1,len1,len2)
        else:
            return max(self.LCS(A,B,i+1,j,len1,len2),self.LCS(A,B,i,j+1,len1,len2))

#Approach 2(Memoization):
class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        len1=len(A)
        len2=len(B)
        mem=[[-1 for index in range(len2)] for index in range(len1)]
        return self.LCS(A,B,0,0,len1,len2,mem)
    
    def LCS(self,A,B,i,j,len1,len2,mem):
        if i==len1 or j==len2:
            return 0
        elif A[i]==B[j]:
            mem[i][j]= 1+self.LCS(A,B,i+1,j+1,len1,len2,mem)
            return mem[i][j]
        else:
            mem[i][j]=max(self.LCS(A,B,i+1,j,len1,len2,mem),self.LCS(A,B,i,j+1,len1,len2,mem))
            return mem[i][j]

#Approach 3(Dynamic Programming):
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m=len(A)
        n=len(B)
        dp=[[0 for index in range(n+1)] for element in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
