def cal(n1,op,n2):
   
    if op== '+':
        add =n1+n2
        print(n1,op,n2,'=',add)    
    if op =='*':
        mul =n1*n2
        print(mul)
    if op=='-':
        sub =n1-n2
        print(sub)
    if op== '%':
        div = n1/n2
        print(div)
n1 = int(input( 'enter the number:'))

op = str(input('enter the op:' ,))

n2 =int(input('enter the n2:')) 
        
cal(n1,op,n2)
