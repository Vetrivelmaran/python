num= int(input('enter the number :'))
temp = num
sum = 0
while num!=0:
      rem = num%10
      sum = rem**3+sum
      num =num//10
if  temp==sum:
   print('yes num is armstrong ')
else:
   print('not armstrong')