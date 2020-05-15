class Solution(object):
    def maxSubarraySumCircular(self, array):
        """
        :type A: List[int]
        :rtype: int
        """
        #max_subarraysum
        max_current_sum=array[0]
        max_global_sum=array[0]
        
        mini_current_sum=float('inf')
        mini_global_sum=float('inf')
        
        sums=array[0]
        
        for element in array[1:]:
            max_current_sum=max(element,max_current_sum+element)
            max_global_sum=max(max_global_sum,max_current_sum)
            
            mini_current_sum=min(element,mini_current_sum+element)
            mini_global_sum=min(mini_current_sum,mini_global_sum)
            
            sums+=element
            
        
        if max_global_sum>0:
            return max(sums-mini_global_sum,max_global_sum)
        else:
            return max_global_sum
        
        
        