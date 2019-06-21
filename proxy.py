t=int(input())

while t:
    d=int(input())
    ip=input().strip()
    pcount=ip.count('P')
    originalpcount=pcount
    attendence=pcount/d
    if(attendence>=0.75):
        print(0)
    else:
        for i,e in enumerate(ip[2:d-2]):
            if e=='A':
                if (ip[i+2-1]=='P' or ip[i+2-2]=='P') and (ip[i+2+1]=='P' or ip[i+2+2]=='P'):
                    pcount+=1
                    attendence=pcount/d
                    if attendence>=0.75:
                        break
        else:
            if attendence<0.75:
                print(-1)
        
        if attendence>=0.75:
            print(abs(originalpcount-pcount))

    t-=1
        