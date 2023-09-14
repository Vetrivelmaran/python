l1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]
new = dict()
for item in l1:
    if  item in new:
        new[item]+=1
    else:
        new[item]=1
print(new)