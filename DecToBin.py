def desTobin(num):

    if num>=1:
        desTobin(num//2)
        print(num%2,end='')
num = int(input('enetr :'))  # desimal to binar 
desTobin(num)


#-----------------------------using loop----------------------------
"""n = int(input())
rem =''
while n>=1:
    rem=str(n%2)+rem
    n=n//2
print(rem)
    """