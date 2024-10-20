"""problem: https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/I"""

testcase=int(input())

while(testcase!=0):
    n=int(input())
    a=list(map(int, input().split()))

    ans=float('inf')

    for i in range(n):
        for j in range(i+1,n):
            curValue= a[i]+a[j]+(j-i)
            ans=min(ans, curValue)

    print(ans)
    testcase-=1