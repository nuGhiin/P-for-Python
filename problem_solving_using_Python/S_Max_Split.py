"""problem:https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/S?fbclid=IwAR1qi6o8WBDOrdzcZ--U5YO_40SSQmmLbZ8jggB6CFIRqog1ukVL_Z2wK2s"""

s = input().strip()

balCount = 0
splitCount = 0
balS = []
curSubS = ""

for char in s:
    if char == 'L':
        balCount += 1
    else:
        balCount -= 1
    
    curSubS += char

    if balCount == 0:
        splitCount += 1
        balS.append(curSubS)
        curSubS = ""
    
print(splitCount)
for i in balS:
    print(i)
