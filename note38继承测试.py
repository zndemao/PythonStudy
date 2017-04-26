import random as r

class Fish:
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)

    def move(self):
        self.x -= 1
        print('weizi',self.x,self.y)

class GoldFish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    # 重写了__init__的方法，就覆盖其方法
    def __init__(self):
        # 方法1
        # Fish.__init__(self)
        # 方法2
        super().__init__()
        self.hungry=True

    def eat(self):
        if self.hungry:
            print('吃货的梦想是天天吃')
            self.hungry=False
        else:
            print('好了')
                  
# 支持多重继承
