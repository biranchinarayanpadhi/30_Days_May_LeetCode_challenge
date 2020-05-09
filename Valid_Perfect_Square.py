#Optimized Algorothm(O(log(sqrt(N))):
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left=1
        right=num
        while left<=right:
            mid=(left+right)//2
            if mid*mid == num:
                return True
            elif mid*mid>num:
                right=mid-1
            else:
                left=mid+1
                
        return False


#Optimized but no of operation and time complexity is more(O(sqrt(N)):
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        sq_root=1
        while sq_root*sq_root<num:
            sq_root+=1
        
        if sq_root*sq_root == num:
            return True
        else:
            return False