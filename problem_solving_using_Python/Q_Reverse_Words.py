"""problem: https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/Q"""
s = input()

words=s.split()
rev_w=[]
#print(words)
for i in words:
    temp = i[::-1]
    rev_w.append(temp)

final_s= ' '.join(rev_w)
print(final_s)

