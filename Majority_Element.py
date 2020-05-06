#Brute Force Approach(O(N*N))
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicti={}
        count=0
        length_nums=len(nums)
        for element in set(nums):
            for items in nums:
                if element == items:
                    count+=1
            
            dicti[element]=count
            count=0
        
        for element in set(nums):
            if dicti[element]>length_nums//2:
                return element
        
        
        

#Optimized Approach(O(N))
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maps={}
        length=len(nums)
        for element in nums:
            if element not in maps:
                maps[element]=1
            else:
                maps[element]+=1
                
        for key,value in maps.items():
            if value>length//2:
                return key

