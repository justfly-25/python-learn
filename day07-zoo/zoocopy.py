class Animal:

   def __init__(self,name,age):
     self.name = name
     self.age = age

   def speak(self):
    return "...."

   def eat(self):
    return f"{self.name}再吃东西"

   def show_info(self):
     return f"{self.name}{self.age}岁——叫声： {self.speak()}"


class Cat(Animal):

   def __init__(self, name, age, breed="中华田园猫"):
      super().__init__(name, age)
      self.breed = breed

   def speak(self):
      return "喵喵"
   
   def scratch(self):
      return f"{self.name}在磨爪子!"
   
class Dog(Animal):
    
    def __init__(self, name, age, breed="中华田园犬"):
       super().__init__(name, age)
       self.breed = breed

    def speak(self):
       return "汪汪"
    def wag_tail(self):
       return f"{self.name}在吃粑粑"
    
class Bird(Animal):
   def __init__(self, name, age, breed="d👁️x👁️r", can_fly=True):
      super().__init__(name, age)
      self.breed =breed
      self.can_fly = can_fly
   def speak(self):
      return "i am a king"
   def get_mad(self):
      return f"{self.name}在发疯"
   def fly_ability(self):
      if self.can_fly:
         return f"{self.name}在飞"
      else:
         return f"{self.name}不会飞"
         
def zoo_announce(animals):
      for animal in animals:
         print(f" {animal.show_info()}")
      for animal in animals:
         print(f" {animal.eat()}")

if __name__ == "__main__":
   cat = Cat("ishot",2,"英短")
   dog = Dog("found",3,"金毛")
   bird = Bird("dexer",1)
   penguin = Bird("QQ",1,can_fly=False)

   print(cat.show_info())
   print(dog.show_info())
   print(bird.show_info())
   print(penguin.show_info())

   zoo_announce([cat, dog, bird, penguin])

   print(f"ishot是猫吗?{isinstance(cat, Cat)}")
   print(f"ishot是动物吗?{isinstance(cat,Animal)}")
   print(f"ishot是狗吗?{isinstance(cat,Dog)}")


   

       
