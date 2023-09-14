n = int(input('enter the number :'))
new =[]
count=0
for i in range(0,n+1):
    num=int(input('enter the number'))

    new.append(num)

avr = sum(new)/n
print(avr)