class Solution:
    def checkStraightLine(self, cordinates: List[List[int]]) -> bool:
        if len(cordinates) <=2:
            return True
        
        y1=cordinates[0][1]
        y2=cordinates[1][1]
        x1=cordinates[0][0]
        x2=cordinates[1][0]
        if x2-x1 == 0:
            return False
        slope=(y2-y1)/(x2-x1)
        
        for index in range(2,len(cordinates)):
            current_point=cordinates[index]
            previous_point=cordinates[index-1]
            y1=previous_point[1]
            y2=current_point[1]
            x1=previous_point[0]
            x2=current_point[0]
            if x2-x1 == 0:
                return False
            new_slope=(y2-y1)/(x2-x1)
            if slope != new_slope:
                return False
        return True
            
        
        