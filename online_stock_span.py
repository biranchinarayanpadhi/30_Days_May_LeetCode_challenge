#Brute Force Approach(O(N^2))-TLE:
class StockSpanner:

    def __init__(self):
        self.array=[]
        self.length=0
        
    def next(self, price: int) -> int:
        if self.length==0:
            self.array.append(price)
            self.length+=1
            return 1
        else:
            count=1
            self.array.append(price)
            self.length+=1    
            if price>=self.array[-2]:
                actual_length=self.length-2
                while actual_length>=0:
                    if self.array[actual_length]<=price:
                        count+=1
                    else:
                        break
                    actual_length-=1
                return count
            return 1
            

#Approach 2(Optimized and Accepted-0(N) without Stack):
class StockSpanner(object):

    def __init__(self):
        self.array=[]
        self.length=0
        self.dicti={}
        
    def next(self, price):
        
        if self.length==0:
            self.dicti[price]=[1,-1]
            self.array.append(price)
            self.length+=1
            return 1
        
        self.array.append(price)
        self.length+=1
        previous_ele=self.array[-2]
        if previous_ele>price:
            if price in self.dicti:
                self.dicti.pop(price)
            return 1
        else:
            count=1
            if previous_ele in self.dicti:
                if self.dicti[previous_ele][1] < 0:
                    self.dicti[price]=[self.dicti[previous_ele][0]+1,-1]
                    return self.dicti[price][0]
                else:
                    last_visited=self.dicti[previous_ele][1]
                    while last_visited>=0:
                        if self.array[last_visited]<=price:
                             count+=1
                        else:
                            break
                        last_visited-=1
                    self.dicti[price]=[count+self.dicti[previous_ele][0],last_visited]
                    return self.dicti[price][0]

            else:
                actual_length=self.length-2
                while actual_length>=0:
                    if self.array[actual_length]<=price:
                        count+=1
                    else:
                        break
                    actual_length-=1
                self.dicti[price]=[count,actual_length]
                return count


#Approach 3(Without Stack- Bit optimized than preivous one):
class StockSpanner(object):

    def __init__(self):
        self.prices=[]
        self.length=0
        self.dicti={}
        
    def next(self, price):
        
        if self.length==0:
            self.dicti[price]=1
            self.prices.append(price)
            self.length+=1
            return 1
        
        self.prices.append(price)
        self.length+=1
        previous_ele=self.prices[self.length-2]
        
        if previous_ele>price:
            self.dicti[price]=1
            return 1
        else:
            index=self.length-2
            while index>=0 and price>=self.prices[index]:
                index-=self.dicti[self.prices[index]]
            
            span_of_price=self.length-1-index
            self.dicti[price]=span_of_price
            return span_of_price
        


#Approach 4(Stack Solution):
class StockSpanner(object):
    def __init__(self):
        self.stack = []

    def next(self, price):
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight