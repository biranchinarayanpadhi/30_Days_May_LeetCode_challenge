# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=0
        high=n
        while True:
            
            if high>=low:
                
                mid=(low+high)//2
                if isBadVersion(mid-1) == False and isBadVersion(mid) == True:
                    return mid
                elif isBadVersion(mid-1) == True and isBadVersion(mid) == True :
                    high=mid-1
                else:
                    low=mid+1
        
            
            
        
        