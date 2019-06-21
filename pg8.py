AccBal=0
while True:
    ip=input()
    if not ip:
        break
    else:
        l=ip.split()
        if l[0]=='D':
            AccBal+=int(l[1])
        else:
            AccBal-=int(l[1])
    
print(AccBal)