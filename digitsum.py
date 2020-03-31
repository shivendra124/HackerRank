# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter


n = int(input())

lst = list((map(int,input().split(" "))))
    
mean = sum(lst)/n
lst.sort()
median = None
if n%2==0:
    median = (lst[int(len(lst)/2-1)]+lst[int(len(lst)/2)])/2
else:
    median = round(len(lst)/2)    
res = Counter(lst)
mode = res.most_common(1)[0][0]

print(mean)
print(median)
print(mode)


