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

#to get list's indexes:
numbers=[12, 34, 55, 63, 32324]
for i, num in enumerate(numbers):
    print(i, num)

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



###         tuples          ###
"""Python tuples are a type of data structure that is very similar to lists. 
The main difference between the two is that tuples are immutable, 
meaning they cannot be changed once they are created.
 This makes them ideal for storing data 
 that should not be modified, such as database records."""

def multiple():
    return 3, 4
print(multiple())
things='pen', 'tripod', 'water bottle'
print(things)
print(type(things))

if 'phone' in things:
    print('exists')

for item in things:
    print(item)

mega =([2, 3, 4], [4, 5, 6]) #2 list inside a tuple
print(mega[0])
mega[0][2]=444 #changing list's value inside of the tuple
print(mega)

###         SET         ###
numbers=[1,2, 3, 4, 5, 6, ]
print(numbers)
n_set=set(numbers)
print(n_set)

#list--> []
#tuple--> ()
#set--> {}
n_set.add(55)
print(n_set)

a={2, 3, 4}
b={5, 6, 7, 4}
print(a&b) #intersection set

print(a|b) #union set
"""
--> SET is full of unique items. No place for duplicates
--> Mutable but doesn't support indexing
"""

###         DICTIONARY          ###
person1=['Kala Miah', 'Kalipur', 34, 'Bekar']
# key value pair
#dictionary
#object
#hash table
#overlap with set
#{key: value}
"""A Python dictionary is a DS & collection of 
key:value pairs"""

person={'name': 'Roshik Kalia', 'address': 'Kalipur', 'age': 24}
print(person)
print(person['age'])
print(person.keys())
print(person.values())
person['name'] = 'Sada Pakhi' # value mutable
print(person)

#dictionary looping:
for item in person:
    print(item) # only keys will be in output
for item in person.items():
    print(item) # to get the values


###         Built in Modules            ###
from math import *
from random import *
from time import sleep

res = ceil(4.456)
res = floor(4.456)
print(res)

print(randint(1,100))
sleep(4)

print('storng')
print(choice(['sakib', 'mash', 'mush']))


###          External packages: PyAutoGUI            ###

import pyautogui
from time import sleep

sleep(5)
for i in range(0, 3):
    pyautogui.write('Hellow Tonmoy', interval=0.25)
    pyautogui.press('enter')


import cv2

cam = cv2.VideoCapture(1)
while True:
    _, frame = cam.read()
    cv2.imshow('my cam',frame)
    cv2.waitKey(1)

###         Exception Handling          ###

try:
    res=47/0
except:
    print('error!')
finally:
    print("finally here!")

print("OKay! Let's try something else.")

###             Python flie read and write          ###

#.csv : comma separated value
#.txt : text file

with open('message.txt', 'w') as file:
    file.write('I Love you Moharani!')
with open('message.txt', 'a') as file:
    file.write('I Love you Moharani!')
with open('message.txt', 'r') as file:
    file.write('I Love you Moharani!')


###         Lambda Function         ###

# def doubled(x):
#     return x*2

doubled = lambda num: num*2 # lambda function
res=doubled(44)
print(res)

add = lambda x, y: x+y
sum= add(1,3)
print(sum)

numbers = [11, 23, 44, 56, 77, 98, 99, 29]
doubled_nums= map(doubled, numbers)
sq_numbers= map(lambda x: x*x, numbers)
print(list(doubled_nums))
print(list(sq_numbers))


actress= [
    {'name': 'Natalie', 'age': 47},
    {'name': 'Kate', 'age': 52},
    {'name': 'Ronan', 'age': 32},
    {'name': 'Saliha', 'age': 28}
]
jr = filter(lambda artist: artist['age'] < 35, actress)
print(list(jr))

fivers= filter(lambda art: art['age'] %5==0, actress)
print(list(fivers))