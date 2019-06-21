ip=list(map(int,input().split(',')))
l=[x**2 for x in ip if x%2]
print(l)
