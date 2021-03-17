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
    def __init__(self, name):
        self.name = name
        #self.age = age
    
    def introduce(self):
        print("hello my name is", self.name )
    
    def eat(self):
        print(self.name , "is eating..")

class Mammalia(Annimal):
     def produce(self):
        print(self.name , "분만가능")

class Pisces(Annimal):
     def swimming(self):
        print(self.name , "수영가능")

class Birds(Annimal):
     def flying(self):
         print(self.name , "비행가능")

class Reptiles(Annimal):
     def metamorphosis(self):
         print(self.name , "변태가능")

class Earth():
    def __init__(self):
        self.pisces = []
        self.mammalia = []
        self.birds = []
        self.reptiles = []
    
    def show_animals(self, animal_type="all"):
        target = []
        if (animal_type == "pisces"):
            target = self.pisces
        elif (animal_type == "mammalia"):
            target = self.mammalia
        elif (animal_type == "birds"):
            target = self.birds
        elif (animal_type == "reptiles"):
            target = self.reptiles
        if (animal_type == "all"):
            print("There are", len(self.pisces), "pisces.")
            #for animal in self.pisces:
                #print(animal.introduce())
            print("There are", len(self.mammalia), "mammalia.")
           # for animal in self.mammalia:
                #print(animal.introduce())
            print("There are", len(self.birds), "birds.")
           # for animal in self.birds:
               # print(animal.introduce())
            print("There are", len(self.reptiles), "reptiles.")
           # for animal in self.reptiles:
               # print(animal.introduce())
        else:
            for animal in self.target:
                print(animal.introduce())
                
            
    
    def add_annimal(self, annimal):
        # isinstance(인스턴스화 된 오브젝트, 검사하고싶은 클래스) == True / False
        # super 상위클래스를 바로 사용할수있는 접근인자 키워드
        if ( isinstance(annimal, Pisces) ):
            self.pisces.append(annimal)
        
        if ( isinstance(annimal, Mammalia) ):
            self.mammalia.append(annimal)
        
        if ( isinstance(annimal, Birds) ):
            self.birds.append(annimal)
        
        if ( isinstance(annimal, Reptiles) ):
            self.reptiles.append(annimal)

    
    def loop(self):
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
    def loop_2(self):
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
