import math
c=50
h=30
d=list(map(int,input().split(',')))
l=[]
for i in d:
    l.append(int(math.sqrt((2*c*i)/h)))
print(l)