class Solution:
    def findComplement(self, num: int) -> int:
        binary_num=bin(num).replace("0b", "")
        complement_binary=""
        for bits in binary_num:
            if bits == "1":
                complement_binary+="0"
            else:
                complement_binary+="1"
        
        final_num=0
        length=len(complement_binary)-1
        for i in complement_binary:
            final_num+=(2**length)*int(i)
            length-=1
        
        return final_num