
for j in range(1,100):
    count=0
    for i in range(1,j+1):
        if j%i==0:
            count +=1
    if count==2:
        print(j)

        
   
