"""problem: https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/G"""
n = int(input())
a = list(map(int, input().split())) 

rev_a = a[::-1]
if rev_a == a:
    print("YES")
else:
    print("NO")