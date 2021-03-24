import time

# class Annimal():
#     def __init__(self, name):
#         self.name = name
#     
#     def sleep(self):
#         print(self.name, "is sleeping...")
#         
#     def walk(self, distance):
#         print(self.name, "is walking ", distance, "km.")
#         
# class Cat(Annimal):
#     def walk(self, distance):
#         print(self.name, "is walking fast", distance * 2, "km")
#     
#     def yaong(self):
#         print(self.name, "say yaong")
# 
# class Dog(Annimal):
#     def __init__(self):
#         self.name = "toto"
#     
#     def wall(self):
#         print(self.name, "say wall")
#         
#         
# 동물
# 
# 포유류 어류 조류 파충류
# 
# 포유류
# 인간 개 고래
# 
# 어류
# 갈치  황태
# 
# 조류
# 비둘기 참새
# 
# 파충류
# 도마뱀 악어

# 클래스를 상속 받을때 마다 상위 클래스의 메서드 오버라이딩 한개 그리고 메서드 추가 한개를 해야한다

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

class Birds(Annimal):
    def eat(self,food):
        if(isinstance(food,Reptiles)):
            food.die()

class Reptiles(Annimal):
    def eat(self,food):
        if(isinstance(food,Mammalia)):
            food.die()

class Earth():
    def __init__(self):
        self.animal=[]
    
            
    
    def add_annimal(self, annimal):
        # isinstance(인스턴스화 된 오브젝트, 검사하고싶은 클래스) == True / False
        # super 상위클래스를 바로 사용할수있는 접근인자 키워드
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
