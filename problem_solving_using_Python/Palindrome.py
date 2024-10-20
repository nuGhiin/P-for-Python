"""problem: https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/I """

n = str(input())
rev_n = n[::-1].lstrip('0')
if  n == rev_n :
    print(rev_n)
    print("YES")
else:
    print(rev_n)
    print("NO")