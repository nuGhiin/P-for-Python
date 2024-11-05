"""class, method, instance"""

class Phone: 
    price = 23000
    color = 'red'
    model = 'samsung'


    def call(self): ##method
        print('are you calling me?')
    
    def sendSMS(self, phone, sms): # self to refer to current instance of the class
        text = f'sending SMS to: {phone} and message: {sms}'
        return text

myPhone = Phone() # creating instance of the phone class. An instance is a specific object created from a class.
print(myPhone.model) # accessing properties by using instance
myPhone.call()
res=myPhone.sendSMS( 17175869, 'who you?')
print(res)


""" constructors """
class Phone: 
    price = 23000
    color = 'red'
    model = 'samsung'
    madeBy = 'china'

    def __init__(self, owner, brand, price): #constructor
        self.owner = owner
        self.brand = brand
        self.price = price


    def call(self): ##method
        print('are you calling me?')
    
    def sendSMS(self, phone, sms): # self to refer to current instance of the class
        text = f'sending SMS to: {phone} and message: {sms}'
        return text


tonmoyPhone = Phone('Tonmoy', 'Samsung', 16000)
print(tonmoyPhone.owner, tonmoyPhone.brand, tonmoyPhone.price)


""" class attributes v/s instance attributes """

class Shop:
    cart = [] # class attribute #shared by all instance of the shop

    def __init__(self, buyer):
        self.buyer = buyer
    
    def addToCart(self, item):
        self.cart.append(item)

tonmoy = Shop('ton moy')
tonmoy.addToCart('watch')
print(tonmoy.cart)

tanjid = Shop('tan jid')
tanjid.addToCart('car')
print(tanjid.cart)

class Shop:
    mall = 'Jamuna'
    
    def __init__(self, buyer):
        self.buyer =buyer
        self.cart = [] #instance atribute
    def addToCart(self,item):
        self.cart.append(item)
    

tonjid = Shop('ton jid')
tonjid.addToCart('house')  
print(tonjid.cart)

tanmoy = Shop('tan moy')
tanmoy.addToCart('plot')
print(tanmoy.cart)

###         Shopping Checkout & Price Calculation            ###

class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
    
    def addToCart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
        print('total price: ', total)
        if amount <total:
            print( f'please provide {total - amount} more')
        else:
            extra = amount -total
            print(f'Here is your items and remaining {extra}')



tonmoy = Shopping('T Tonmoy')
tonmoy.addToCart('alu', 50, 6)
tonmoy.addToCart('bread', 25, 5)

print(tonmoy.cart)

tonmoy.checkout(1469)





###         Create a school using multiple classes          ###

class Student:
    def __init__(self, name, id, cclass):
        self.name = name
        self.id = id
        self.cclass = cclass
    
    def __repr__(self) -> str: ## to display the class in readable way
        return f'Student infos: name: {self.name}, class: {self.cclass}, id: {self.id}'

class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id
    
    def __repr__(self) -> str:
        return f'Teacher infos: name:{self.name}, subject: {self.subject}, id: {self.id}'

class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
    
    def addTeachers(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)
    
    def enroll(self, name, fee):
        if fee < 6500:
            return 'not enough fees'
        else:
            id = len(self.students) + 1
            student = Student(name, id, 'C')
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'

    def __repr__(self) -> str:
        print('Welcome to ', self.name)
        print('------Our Teachers------')
        for teacher in self.teachers:
            print(teacher)
        print('------OUr Students-------')
        for student in self.students:
            print(student)
        return 'All Done'




darunSchool = School('Darun School')
darunSchool.enroll('tanjid', 8799)
darunSchool.enroll('tanmid', 8739)
darunSchool.enroll('tandid', 7399)
darunSchool.enroll('tansis', 6599)

darunSchool.addTeachers('Prof Rohama', 'Quantam Physics')
darunSchool.addTeachers('Prof Tonmoy', 'Algorithm Advance')
darunSchool.addTeachers('Prof Mehzabin', 'DBMS')


print(darunSchool)


tonmoy = Teacher('T Tonmoy', 'Chemistry', 20147)
print(tonmoy)
alia = Student('Aila Bhaat', 93838, 9)
print(alia)





