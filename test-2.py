import time
import random

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
            return(False)#살아있다
        
        else:
            return(True)#죽어있다
    #def if_die(self):
    #return (not self.__alive)



class Mammalia(Annimal):
    def eat(self,food):
        if(isinstance(food,Pisces)):
            food.die()
            print("eating pisces")

    def reproduce(self,annimal):
        if(isinstance(annimal,Mammalia)):
            new_mammalia = Mammalia()
            return(new_mammalia)
                 
class Pisces(Annimal):
    def eat(self,food):
        if(isinstance(food,Birds)):
            food.die()
            print("eating birds")

    def reproduce(self,annimal):
        if(isinstance(annimal,Pisces)):
            new_pisces = Pisces()
            return(new_pisces)
class Birds(Annimal):
    def eat(self,food):
        if(isinstance(food,Reptiles)):
            food.die()
            print("eating reptiles")

    def reproduce(self,annimal):
        if(isinstance(annimal,Birds)):
            new_birds = Birds()
            return(new_birds)
class Reptiles(Annimal):
    def eat(self,food):
        if(isinstance(food,Mammalia)):
            print("eating mamalia")
            food.die()

    def reproduce(self,annimal):
        if(isinstance(annimal,Reptiles)):
            new_reptiles = Reptiles()
            return(new_reptiles)
class Earth():
    def __init__(self):
        self.annimal=[]#4마리의 종류를 넣어놓는다.
    
    def add_annimal(self, annimal):
        self.annimal.append(annimal)

    
    def reproduce_phase(self):#
        for a in range(int(len(self.annimal)/2)):
            self.add_annimal(self.annimal[a].reproduce(self.annimal[a+int(len(self.annimal)/2)]))
        
    
    def eat_phase(self):
        for a in range(int(len(self.annimal)/2) - 1):
            self.annimal[a].eat(self.annimal[a+int(len(self.annimal)/2) - 1])
   
    
    def check_die_annimal(self):
        self.annimal = [a for a in self.annimal if a != None] # not useful
        updated_annimal = [a for a in self.annimal if a.if_die() == False]
        del self.annimal
        self.annimal = updated_annimal

    def loop(self):
        while(True):
            random.shuffle(self.annimal)
            self.reproduce_phase()
            self.eat_phase()
            self.check_die_annimal()
            print(len(self.annimal))
                
earth = Earth()
fish = Pisces()
human = Mammalia()
sparrow = Birds()
lizard = Reptiles()
earth.add_annimal(fish)
earth.add_annimal(human)
earth.add_annimal(sparrow)
earth.add_annimal(lizard)
earth1 = Earth()
fish1 = Pisces()
human1 = Mammalia()
sparrow1 = Birds()
lizard1 = Reptiles()
earth.add_annimal(fish1)
earth.add_annimal(human1)
earth.add_annimal(sparrow1)
earth.add_annimal(lizard1)
earth.loop()

# [p, m, b, r]


# 재귀함수
# 성능의 차이 반복문은 리미트가있다 재귀함수는 리미트가없다.(속도가빠르다)
# [1,2,3]

# 환경의규칙ex) 파충류는 2 마리있으면 번식한다 생태계룰.
# 번식과 잡아먹기. <- 코딩해보기 먹이 사슬을 만들어서.
