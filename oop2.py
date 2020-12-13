import math


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def distance(self,other):
        cos_d=math.sin(self.x)*math.sin(other.x)+math.cos(self.x)*math.cos(other.x)*math.cos(self.y-other.y)
        return 6371*math.acos(cos_d)



class City(Point):
    def __init__(self,x,y,name,pop):
        super().__init__(x,y)
        self.name=name
        self.pop=pop

Moscow=City(55.7522200,37.6155600,"Москва",12615882)
Chelyabinsk=City(55.154,61.4291,"Челябинск",1200703)

print(Moscow.distance(Chelyabinsk))
