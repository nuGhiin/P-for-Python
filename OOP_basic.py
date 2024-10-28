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
