def mergesort(a):
    if len(a)>1:
        mid =len(a)//2
        l =a[:mid]
        r =a[mid:]
        mergesort(l)
        mergesort(r)
        a.clear()
        while len(l)>0 and len(r)>0:
            if l[0]<=r[0]:
                a.append(l[0])
                l.pop(0)
            else:
                a.append(r[0])
                r.pop(0)
        for i in l:
            a.append(i)
        for i in r:
            a.append(i)

a=[]
n = int(input('enter the number of list:'))
for i in range(n):
    a.append(int(input('enetr the number:')))
print(a)
mergesort(a)
print(a)