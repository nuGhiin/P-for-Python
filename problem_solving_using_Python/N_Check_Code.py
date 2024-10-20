"""problem: https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/N"""

a, b = map(int, input().split())
s=input()

if s[a] == '-' and s[:a].isdigit() and s[a+1:].isdigit():
    print("Yes")
else:
    print("No")
