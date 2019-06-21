'''
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

ip=input()
lcount=dcount=0
for i in ip.split():
    for j in i:
        if j.isdigit():
            dcount+=1
        elif j.isalpha():
            lcount+=1
        else:
            pass
        
print(f'LETTERS:{lcount}\nDIGITS:{dcount}')