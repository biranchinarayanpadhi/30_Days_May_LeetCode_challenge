#Optimzed_Approach(O(N)):
class Solution:
    def countBits(self, num: int) -> List[int]:
        result=[0]*(num+1)
        for element in range(num+1):
            result[element]=result[element//2]+element%2
        return result
            
#Brute Force(O(N*sizeof(integer))):
class Solution:
    def countBits(self, num: int) -> List[int]:
        number=2
        count=0
        result=[0,1]
        if num == 0:
            return [0]
        while number<=num:
            temp=number
            strs=""
            while temp!=0:
                strs+=str(temp%2)
                temp//=2
            result.append(strs.count("1"))
            number+=1
        return result
        
#Approach 3(Bit optimized than Brute Force):
class Solution:
    def countBits(self, num: int) -> List[int]:
        number=2
        count=0
        result=[0,1]
        if num == 0:
            return [0]
        while number<=num:
            temp=number
            strs=[]
            count=0
            while temp!=0:
                if temp%2 == 1:
                    count+=1
                temp//=2
            result.append(count)
            number+=1
        return result
        
