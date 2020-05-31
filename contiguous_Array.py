#Optimized Approach(O(N))
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        dicti={}
        maxi=0
        length=len(nums)
        dicti[0]=-1
        for index in range(length):
            
            if nums[index] == 0:
                count-=1
                
            elif nums[index] == 1:
                count+=1
            
            if count in dicti:
                maxi=max(maxi,index-dicti[count])
            else:
                dicti[count]=index
        return maxi