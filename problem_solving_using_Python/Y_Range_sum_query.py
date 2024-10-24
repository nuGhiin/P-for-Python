"""problem: https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/Y"""

m, n = map(int,input().split())
a = list(map(int, input().split()))

preSum = [0] * (m+1)
for i in range(1, m+1):
    preSum[i] = preSum[i-1] + a[i-1]


for i in range(n):
    p, q = map(int, input().split())
    total =preSum[q] - preSum[p-1]
    print(total)
    
    
    
    #print(sum(a[p-1:q]))
    # total =0
    # for j in range(p-1, q):
    #     total+=a[j]
    # print(total)



