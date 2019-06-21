t=int(input())
while t:
    n=int(input())
    digitsum=0
    temp=n
    while temp:
        digitsum+=temp%10
        temp//=10
    rn=10-digitsum%10
    res=10*n+rn
    print(res)
    t-=1

