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