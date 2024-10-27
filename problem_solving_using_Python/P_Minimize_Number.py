"""problem: https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/P"""

n = int(input())
a = list(map(int, input().split()))
cnt =float('inf')
flag = False

for i in range(n):
    if a[i]%2!=0:
        flag = True
    else:
        divisions=0
        while a[i] %2 == 0:
            a[i]=a[i]//2
            divisions+=1
        cnt = min(cnt, divisions)
        
if flag == True:
    print(0)
else:
    print(cnt)
    
        