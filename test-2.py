import time

class Annimal():
    def __init__(self):
        self.__alive = True

    
    def sleep(self):
        pass

    def reproduce(self,annimal):
        pass

    def eat(self):
        pass

    def die(self):
        self.__alive = False

    def if_die(self):
        if(self.__alive == True):
            return(False)
        
        else:
            return(True)
    #def if_die(self):
    #return (not self.__alive)



class Mammalia(Annimal):
    def eat(self,food):
        if(isinstance(food,Pisces)):
            food.die()
    def reproduce(self,annimal):
        if(isinstance(annimal,Mammalia)):
            new_mammalia = Mammalia()
            return(new_mammalia)
                 
class Pisces(Annimal):
    def eat(self,food):
        if(isinstance(food,Birds)):
            food.die()
    def reproduce(self,annimal):
        if(isinstance(annimal,Pisces)):
            new_pisces = Pisces()
            return(new_pisces)
class Birds(Annimal):
    def eat(self,food):
        if(isinstance(food,Reptiles)):
            food.die()
    def reproduce(self,annimal):
        if(isinstance(annimal,Birds)):
            new_birds = Birds()
            return(new_birds)
class Reptiles(Annimal):
    def eat(self,food):
        if(isinstance(food,Mammalia)):
            food.die()
    def reproduce(self,annimal):
        if(isinstance(annimal,Reptiles)):
            new_reptiles = Reptiles()
            return(new_reptiles)
class Earth():
    def __init__(self):
        self.animal=[]
    
            
    
    def add_annimal(self, annimal):
        self.animal.append(annimal)

    
    def reproduce_phase(self):
        if len(self.pisces) >= 2:
            new_fish = Pisces("fish")
            self.pisces.append(new_fish)
        if len(self.mammalia) >= 2:
            new_mammalia = Mammalia("mammalia")
            self.mammalia.append(new_mammalia)
        if len(self.birds) >= 2:
            new_birds = Birds("birds")
            self.birds.append(new_birds)
        if len(self.reptiles) >= 2:
            new_reptiles = Reptiles("lizad")
            self.reptiles.append(new_reptiles)  
    
    def eat_phase(self):
        if len(self.pisces) >3:
            self.pisces.pop()
            print("물고기 사람이 잡아먹었다") 
        if len(self.mammalia) >3:
            self.mammalia.pop()
            print("고래 사람이 잡아먹었다")
        if len(self.birds) >3:
            self.birds.pop()
            print("새 사람이 잡아먹었다")
        if len(self.reptiles) >3:
            self.reptiles.pop()
            print("파충류 사람이 잡아먹었다")
                
earth = Earth()
fish = Pisces("다금바리")
human = Mammalia("사람")
sparrow = Birds("참새")
lizard = Reptiles("도마뱀")
earth.add_annimal(fish)
earth.add_annimal(fish)
earth.add_annimal(human)
earth.add_annimal(human)
earth.add_annimal(sparrow)
earth.add_annimal(sparrow)
earth.add_annimal(lizard)
earth.add_annimal(lizard)
while (True):
    time.sleep(1)
    earth.loop()
    earth.loop_2()
    earth.show_animals()


# 재귀함수
# 성능의 차이 반복문은 리미트가있다 재귀함수는 리미트가없다.(속도가빠르다)
# [1,2,3]

# 환경의규칙ex) 파충류는 2 마리있으면 번식한다 생태계룰.
# 번식과 잡아먹기. <- 코딩해보기 먹이 사슬을 만들어서.
