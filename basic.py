#taking input:
from sys import argv


input("Give me money: ")
money = input("Give me money: ")
print("Here is your money: ", money)
print(type(money))

#type-casting
money_int=int(money)


print(56/3) # vagfol
print(56%3) # reminder
print(56//3) #purno vagfol

#power 
power = 2**3
print(power)

#if-else condition:

a = 2
if a>2:
    print('true')
elif a>1:
    print('ok')
else:
    print('false')


#while-loop:
num =1
while num<=10:
    print(num)
    num+=1

#for-loop:
numbers =[5, 10, 15, 20, 25]
for num in numbers:
    print(num)

for i in range(1, 10, 2): #(start, stop, step)
    print(i)

sentence="You are my everything!"
for char in sentence:
    print(char)

for i in range(5):
    print(i) #output: 0 1 2 3 4


###### F U N C T I O N #######
def double_int(num):
    sum=num*2
    print(sum)
double_int(8)

def calc(n1, n2):
    sum=n1**n2
    return sum
total =calc(2,2)
print('TValue: ', total)

#args
def allSum(*numbers): #will take as many parameters as needed
    print(numbers)

total=allSum(1, 2, 3 ,4)
print('total: ', total)

def all_Sum(n1, n2, *args): #formally called as args
    sum=n1+n2
    for i in args:
        print(i)
        #sum=sum+i
    return sum
t=all_Sum(10, 20, 30, 40, 50)
print("Total: ", t)


def name(firstName, lastName):
    name=f'full name is: {firstName} {lastName}' #fString
    #name = firstName + ' ' + lastName
    return name

#HisName = name('Rakib', 'Khan') #taking parameeters in order

HisName = name(lastName='islam', firstName='tonmoy') # in python order is not mandatory

print(HisName)

#kargs- [key argument]:
def famousName(first, last, **addition):
    name = f'{first} {last}'
    #print(addition['title'])
    for key, value in addition.items():
        print(key, value)

    return name

name=famousName(first='Athar', last='Ali', title='sahebzada', title2='khan', last2='Talukder')
print(name)

#retun multiple things from an array
def a_lot(n1, n2):
    sum=n1+n2
    mult=n1*n2
    remain = n1-n2
    return [sum, mult, remain]
    #return sum, mult, remain

res=a_lot(10,20)
print(res)

##global and local scope:

balance = 3000 #global var

def buyThing(item, price):
    #local scope var
    #can access global var without using the global var
    dreamPhone ='Iphone'
    # to modify , have to use the global keyword
    global balance
    print(f' privious balance value ', balance)
    balance =balance -price
    print(f'balance after buying {item}', balance)

buyThing('Laptop', 2000)
print("After shopping: ", balance)


"""L I S T"""

#index =  0  1   2    3   4   5   6   7   8
numbers= [45,50, 55, 32, 27, 87, 39, 77, 99]
#index = -10  -9  -8  -7  -6  -5  -3  -2   -1

print(numbers[3], numbers[-3])

#list(start:end) start from the begining index and stops before the end index
print(numbers[1: 4])
#list(star: end: step)
print(numbers[2:8:2])
print(numbers[8:2:-2])
print(numbers[:4]) #0 theke shuru hoye 4 er aag porjonto cholbe
print(numbers[3:]) # 3 theke shuru hoye shesh index er aag porjonto cholbe
print(numbers[:])  # shortcut to copy / shuru theke shesh index er purbo porjonto
print(numbers[: : -1]) #shortcut to reverse


###LIST Comprehension###

numbers = [11, 23, 44, 56, 77, 98, 99, 29]
odds=[]
for num in numbers:
    if num%2 == 1:
        odds.append(num)
print(odds)

oddsNumbers = [num for num in numbers if num%2 == 1]
print(oddsNumbers)

numbers =[7,8,5,4,3,2,4]
print(numbers[::-1])

###         String        ###

name='sakib\'s khan'#escape
name2="sakib khan"
name3= """
sakib khan
numver one
"""
print(name)

#string is a sequence of characters
for char in name2:
    print(char)
#mutable means changeable
#immuatable means you can't change it
name2[0]='R' #not allowed / string immutable

