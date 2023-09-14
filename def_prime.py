def prime(n):
    count =0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
start =int(input(''))
end=int(input(''))    
for i in range(start,end):
    if prime(i):
         print(i)

