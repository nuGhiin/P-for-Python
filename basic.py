#taking input:
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


#functions:
def double_int(num):
    sum=num*2
    print(sum)
double_int(8)

def calc(n1, n2):
    sum=n1**n2
    return sum
total =calc(2,2)
print('TValue: ', total)