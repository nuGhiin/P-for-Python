"""problem: https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/M"""

# a, b = input().split()
# a = int(a)  
# b = int(b)  
a, b = map(int, input().split())

lucky = False

for i in range(a, b+1):
    is_lucky = True
    for d in str(i):
        if d!='4' and d!='7':
            is_lucky=False
            break

    if is_lucky:
        print(i, end=" ")
        lucky=True
        
if not lucky:
    print("-1")