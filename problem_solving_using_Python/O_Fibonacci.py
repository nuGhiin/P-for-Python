"""problem: https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/O"""

n = int(input())

fib=[0,1]

if n==1:
    print(0)
elif n==2:
    print(1)
else:
    for i in range(2, n):
        fib.append(fib[i-1]+fib[i-2])
    
    print(fib[n-1])