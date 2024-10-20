"""problem: https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/M"""

n = int(input())

""" to take an array as an input but not in a single line
arr = []
for i in range(n):
    arr.append(int(input(), end=" "))

"""

#to take a list as an input in a single line
arr = list(map(int,input().split()))

maax = max(arr)
miin = min(arr)

for i in range(n):
    if arr[i]==maax:
        arr[i]=miin
    elif arr[i]==miin:
        arr[i]=maax
print(*arr)