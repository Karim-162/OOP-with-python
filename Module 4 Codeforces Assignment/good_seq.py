#https://atcoder.jp/contests/arc087/tasks/arc087_a
from collections import Counter
num=int(input())
remove=0
a=list(map(int,input().split()))
counter=Counter(a)
for number,count in counter.items():
    if number == count:
        continue
    elif number>count:
        remove+=count
    else:
        remove+=count-number
print(remove)
