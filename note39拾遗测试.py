# 拾遗
class Turtle:
    def __init__(self,x):
        self.num=x
        
class Fish:
    def __init__(self,x):
        self.num=x

class Pool:
    def __init__(self,x,y):
        self.turtle=Turtle(x)
        self.fish=Fish(y)

    def print_num(self):
        print('shui chi li you zong gong wu gui %d ,xiao yu %d '% (self.turtle.num,self.fish.num))    
#>>> pool=Pool(1,10)
#>>> pool.print_num()
#shui chi li you zong gong wu gui 1 ,xiao yu 10 
#>>> 
