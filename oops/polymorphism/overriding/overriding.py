#overriding:
'''
overriding refers to the ability of a subclass (child class) to redefine the behavior of a method inherited from its parent class.
'''
#Method overriding:
'''
Python supports method overriding through inheritance.
A subclass can redefine a method inherited from its parent class, 
and child class is allowed to redefine that method in child class based on our requirement. This concept is methodoverriding.

overriding concept is applicable for both methods and constructors.
'''
class hp:        #base class
    def price(self):
        print('HP laptop gets under 50,000')
class Dell(hp):    #sub class inherits the base class properties & redifining
    def price(self):
        print('Dell laptop gets under 60,000')
        
class MAC(hp):      #sub class inherits the base class properties & redifining
    def price(self):
        print('MAC laptop gets under 100000')
        super().price()      #calls base class price method using super keyword.
brand1=hp()       #creating object for the class
brand2=Dell()
brand3=MAC()

brand1.price()      #calling method
brand2.price()
brand3.price()


class Laptop:
  """Base class representing a generic laptop"""
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def info(self):
    print(f"Brand: {self.brand}, Model: {self.model}")

class GamingLaptop(Laptop):
  """Subclass representing a gaming laptop"""
  def __init__(self, brand, model, graphics_card):
    super().__init__(brand, model)  # Call base class constructor
    self.graphics_card = graphics_card

  def info(self):
    super().info()  # Call base class info method
    print(f"Graphics Card: {self.graphics_card}")

class Ultrabook(Laptop):
  """Subclass representing an ultrabook"""
  def __init__(self, brand, model, weight):
    super().__init__(brand, model)  # Call base class constructor
    self.weight = weight

  def info(self):
    super().info()  # Call base class info method
    print(f"Weight: {self.weight} kg")

# Create objects
gaming_laptop = GamingLaptop("Alienware", "M15 R7", "RTX 3070")
ultrabook = Ultrabook("LG", "Gram 17", 1.3)

# Call info method on each object
gaming_laptop.info()
ultrabook.info()


#constructor overriding:
'''
Python doesnt allow multiple constructors with the same name but different argument lists within a class.
If you define multiple methods with the name __init__ in a class, the last definition will override the earlier ones.
we can achieve it by using default arguments
and by using *args and *kwargs
'''