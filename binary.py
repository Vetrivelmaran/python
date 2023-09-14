n=int(input('enter '))
while(n>0):
    s=n%10
    if s!=0 and s!=1:
        print('not binary')
        break
    n=n//10
    if n==0:
        print('binary')