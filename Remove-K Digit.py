#Approach 1 Using Stack
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        index=0
        len_nums=len(num)
        
        if (len_nums == 1 and k == 1) or len_nums == k:
            return "0"
        
        no_of_operation=k
        while index<len_nums:
            element=num[index]
            
            while len(stack)!=0 and stack[-1]>element and no_of_operation>0:
                stack.pop()
                no_of_operation-=1
            
            stack.append(element)
            index+=1
            
        #converting the stack elements to string
        smallest_number="".join(stack)
        
        #removing the leading zeroes if any from the string and returning the substring after removing the string   
        smallest_number=smallest_number.lstrip("0")   
        
        #if smallest_number is an empty stiring it will return 0
        return smallest_number[:len_nums-k] or "0"


#Approach 2(Using Queue-Same logic as above)
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        Queue=[]
        index=0
        len_nums=len(num)
         
        no_of_operation=k
        while index<len_nums:
            element=num[index]
            
            while len(Queue)!=0 and Queue[-1]>element and no_of_operation>0:
                Queue.pop()
                no_of_operation-=1
            
            Queue.append(element)
            index+=1
            
        no_of_character=len_nums-k
        smallest_number=""
        while no_of_character!=0:
            smallest_number+=Queue.pop(0)
            no_of_character-=1
        
        smallest_number=smallest_number.lstrip("0")
        return smallest_number or "0"
       