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

    def show(self):
        return (f"Город {self.name},Население {self.pop}")

class Mountain(Point):
    def __init__(self,x,y,name,height):
        super().__init__(x,y)
        self.name=name
        self.height=height

    def show(self):
        return (f"Название горы {self.name},Высота {self.height}")
        


Moscow=City(55.7522200,37.6155600,"Москва",12615882)
Chelyabinsk=City(55.154,61.4291,"Челябинск",1200703)
Elbrus=Mountain(27.98791,86.98791,"Эльбрус",6794)
Everest=Mountain(46.84931,53.84295,"Эверест",5899)

print(Moscow.distance(Chelyabinsk))
print(Elbrus.distance(Everest))
print(Elbrus.show())
print(Moscow.show())
