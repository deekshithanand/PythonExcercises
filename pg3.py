l=list()
while True:
    
    a=input().strip()
    if len(a)==0:
        break
    l.append(a.upper())
    
for i in l:
    print(i)