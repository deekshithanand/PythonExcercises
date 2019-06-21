'''
Write a program, which will find all such numbersbetween 1000 and 3000 (both included) 
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

op=''
for i in range(1000,3001):
    n=i
    while n:
        d=n%10
        if d%2:
        
            break
        else:
            n=n//10
    else:
        op+=f'{i},'

print(op)