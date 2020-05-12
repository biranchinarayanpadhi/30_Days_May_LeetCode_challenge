#Brute Force Approach(O(logN))
class Solution(object):
    def singleNonDuplicate(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(arr)-1
        
        while left<=right:
            mid=(left+right)//2
            
            print(left,right,mid,mid-1,mid+1) 
            
            if mid-1>=0 and mid+1<=len(arr)-1:
            
                if arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]:
                    return arr[mid]

                elif arr[mid] == arr[mid-1]:
                    if (mid+1)%2==0:
                        left=mid+1
                    else:
                        right=mid-1
                else:
                    if (mid)%2==0:
                        left=mid+1
                    else:
                        right=mid-1
            else:
                return arr[mid]            