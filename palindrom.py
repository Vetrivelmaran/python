n = int(input('enter the number :'))
temp=n
sum = 0
while n!=0:
    
    sum = sum *10 + n%10
    n = n//10
if temp==sum:
    print('palindrom')
else:
    print('not palindrom')
