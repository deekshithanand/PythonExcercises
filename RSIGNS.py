#naive method
t=int(input())
k=int(input())
limit=10**k
modulo=10**9+7
for _ in range(t):
    count=0
    for i in range(limit):
        d1=set(str(i))
        d2=set(str((limit-i-1)))
        if len(d1.union(d2))==2:
            count=(count+1)%(modulo)
    else:
        print(count)
    


