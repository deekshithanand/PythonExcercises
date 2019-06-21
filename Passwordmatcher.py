def pm(pwd):
    pwd=str(pwd)
    flag=False
    if len(pwd)>5 and len(pwd)<13:
        if pwd.isalnum():
            if not pwd.islower():
                if pwd.find('#')!=-1 or pwd.find('$')!=-1 or pwd.find('@')!=-1:
                    flag=True
    return flag


ip=input().split(',')
for i in ip:
    if pm(i):
        print(i)