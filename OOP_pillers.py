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
"""                         Inheritence                                  """
############################################################################

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