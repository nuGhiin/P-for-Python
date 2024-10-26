"""problem: https://atcoder.jp/contests/arc087/tasks/arc087_a"""

from collections import Counter


n = int(input())
a = list(map(int, input().split()))

freq = Counter(a)
rem = 0
for i, count in freq.items():
    if count > i:
        rem += count - i
    elif count < i:
        rem += count
print(rem)
