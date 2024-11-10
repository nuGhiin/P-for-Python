###           Common and uncommon things            ###

class Laptop:
    def __init__(self, brand, price, color, memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory
    
    def run(self):
        return f'Running Laptop: {self.brand}'
    
    def coding(self):
        return f'Learing python & practicing '
    
class Phone:
    def __init__(self, brand, price, color, dual_sim) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.dual_sim = dual_sim
    
    def run(self):
        pass
    
    def phoneCall(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    



############################################################################
"""                         Inheritance                                  """
############################################################################
"""
Inheritance enables reusability , allowing new classes to build upon existing
ones.
"""



#base class/parent class, common attribute + functionality class
#derived class/child class, uncommon attribute + functionality class

class BaseClass: 
    pass

class DerivedClass(BaseClass):
    pass

"""
1. Simple inheritance: parent class --> child class
(Gadget --> Phone) 
(Gadget --> Laptop)

2. Multi-level inheritance: Grand --> parent --> child
(vehicle --> bus --> ac bus)

3. Multiple inheritance: 

4. Hybrid inheritance: 

"""



#simple inheritance
class Gadget:
    def __init__(self, brand, price, color) -> None:
        self.brand = brand
        self.price = price
        self.color = color
    
    def run(self):
        return f'Running Laptop: {self.brand}'
    

    # def __repr__(self) -> str:
    #     return f'{Phone}'



class Laptop:
    def __init__(self, memory) -> None:
        self.memory = memory
    
    def coding(self):
        return f'Learing python & practicing '
    
class Phone(Gadget):
    def __init__(self, dual_sim, brand, price, color) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color)
    
    def phoneCall(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    
    def __repr__(self) -> str:
        return f'Phone: {self.brand} {self.price} {self.dual_sim}'


myPhone = Phone(True, 'Samsung', 105000, 'red')
print(myPhone)


#multilevel inheritance
class Vehicle:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    
    def move(self):
        pass

    def __repr__(self) -> str:
        return f'{self.name} {self.price}'
    

  
class Bus(Vehicle):
    def __init__(self, name, price, seat) -> None:
        self.seat = seat
        super().__init__(name, price)
    
    def __repr__(self) -> str:
        return super().__repr__()

class Truck(Vehicle):
    def __init__(self, name, price, weight) -> None:
        self.weight = weight
        super().__init__(name, price)

class PickUpTruck(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)

class ACBuss(Bus):
    def __init__(self, name, price, seat, temp) -> None:
        self.temp = temp
        super().__init__(name, price, seat)
    
    def __repr__(self) -> str:
        print (f'{self.seat}')
        return super().__repr__()


green_line = ACBuss('GreenLine', 2500, 40, 36)
print(green_line)


#multiple inheritance:

class Family:
    def __init__(self, address) -> None:
        self.address = address

class School:
    def __init__(self, id, level) -> None:
        self.id = id
        self.level = level

class Sports:
    def __init__(self, game) -> None:
        self.game = game

class Student(Family, School, Sports):
    def __init__(self, address, id, level, game) -> None:
        School.__init__(self, id, level)
        Sports.__init__(self, game)
        super().__init__(address)






############################################################################
"""                         Encapsulation                                """
############################################################################
"""
Encapsulation keeps data safe and ensures control over 
modifications.
"""
class Bank:
    def __init__(self, holderName, initDeposit) -> None:
        self.holderName = holderName # public
        self.__balance = initDeposit ## access modifier(private)
        self._branch = 'banani 11' #protected

    def deposit(self, amount):
        self.__balance +=amount

    def get_balance(self):
        return self.__balance

tom = Bank('tanj', 12500)

tom.holderName = 'minaj'
print(tom.holderName)
print(tom.get_balance())

print(tom._Bank__balance)



############################################################################
"""                         Abstraction                                 """
############################################################################
"""
Abstraction: It is the concept of hiding unnecessary details from the user and only showing essential infos.
In python, abstract classes and abstract methods help implement
abstraction. 
- Abstract classes serve as blueprints for other classes, 
ensuring that certain methods are present in subclass without implementing them directly in
abstract class

"""
from abc import ABC, abstractmethod     
#abstraction base class = abc

class Animal(ABC):
    @abstractmethod  #enforcing all derived / child class to have eat method
    def eat(self):
        pass #No implementation here, subclasses must define it

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.category = 'Monkey'
        self.name = name
        super().__init__()
    def eat(self):
        print('I need food')

layka = Monkey('lucky')
layka.eat()


############################################################################
"""                         Polymorphism                                 """
############################################################################
"""
Polymorphism: It means --> many forms.
- It allows objects to be treated as instances of their parent class
rather than their actuall class.
"""
# poly --> many(multiple)
# morph --> tyep

class Animal:
    def __init__(self, name) -> None:
        self.name = name
    def makeSound(self):
        print('animal making their sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def makeSound(self):
        print('meow meow')

mishti = Cat('Mishti')
mishti.makeSound()


class Kutta(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def makeSound(self):
        print('ghew ghew')

lalu = Kutta('Laalu')
lalu.makeSound()

class Goru(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def makeSound(self):
        print('hemba hemba')

mishu = Goru('mishu miah')
mishu.makeSound()

animals = [mishti, lalu, mishu]
for animal in animals:
    animal.makeSound()


print(issubclass(Kutta, Animal))
print(isinstance(mishti, Cat))


class Bird:
    def sound(self):
        return "Chirp"

class Dog:
    def sound(self):
        return "Bark"

def make_sound(animal):
    print(animal.sound())

bird = Bird()
dog = Dog()

make_sound(bird) # Output: Chirp
make_sound(dog)  # Output: Bark



##########################
"""     OOP More    """
##########################


# Overriding: 
"""
It happens when a child(subclass) provides its own version of a method that
is already defined in its parent(superclass). The child class "overrides"
the method of the parent class. It allows to define specialized behavior
in the child class.
- The method in the child class has the same name and same parameters as the method in the
parent classs.
- when , call the overridden method on an object of the child class,
python uses the version of the method defined in the child class.
"""

class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height 
        self.weight = weight
    
    def eat(self):
        print("he is eating")
    
    def exercise(self):
        raise NotImplementedError

class Circketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    #override
    def eat(self):
        print('Under diet')

        
    #overloading + operator
    def __add__(self, other):
        return self.age + other.age




mushfiq = Circketer('Mushfiq', 35, 162, 60, 'BD')
ashfaq = Circketer('Ashfaq', 27, 172, 64, 'DD')
mushfiq.eat()
#mushfiq.exercise()

#overloading + operator
print(mushfiq + ashfaq)



class Shopping:
    cart = [] #class attribute / #static attribute

    def __init__(self, name, age, birthyear) -> None:
        self.name = name
        self._age = age
        self.__birthyear = birthyear


    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'roilo baki: {remaining}')
    
    @classmethod
    def check(cls, ok):
        print('is it okay?')

    """
cls vs self: In instance methods (which lack @classmethod), 
self receives the instance of the class. 
But in a class method, cls receives the class itself, 
allowing it to interact with class-level data.

cls represents the class, a class method can:

--> Access and modify class attributes shared among all instances.
--> Call other class methods or create new instances of the class itself.

"""
    
    @staticmethod
    def addd(a, b): # Static method that doesn't need access to the class or instance
        print('res: ', a+b)
    

    #getter : read only : getter without any setter is read only attribute
    """get a value of property through a method.
    most of time , to get the value of private attribute"""
    @property
    def birthYear(self):
        return self.__birthyear

    #setter
    """set a value of property through a method.
    most of time , to set the value of private attribute"""
    @birthYear.setter
    def birthYear(self, val):
        if val< 0:
            return 'cannot be neg'
        self.__birthyear += val





# mb = Shopping('MB')
# mb.purchase('tshirt', 435, 2) # Using instance method with an instance

# #Shopping.purchase('mb', 'lug', 33, 1)
# #Shopping.check('2', True)
# Shopping.check(True) # Using class method with the class itself

# Shopping.addd(5,6)

samsu = Shopping('sma', 22, 2000)
#print(samsu.__birthyear)

print(samsu.birthYear)
samsu.birthYear = 1
print(samsu.birthYear)


###         inner function and wrapper function         ###

#function is a first class object

def double():
    print('inside double')
    def tripple():
        print('inside tripple')
        return 'inside triple'
    return tripple

print(double()())

def routine(work):
    print('started')
    work()
    print('ended')

def coding():
    print('learning python')

routine(coding)



### how does a decorator work:
import math
def timer(func):
    def inner(*args, **kargs):
        print('time started')
        #print(func)
        func(*args, **kargs)
        print('time ended')
    return inner

@timer
def get_fact(n):
    print('fact gotcha!')
    res = math.factorial(n)
    print(f'factorial of {n} is: {res}')


get_fact(5)