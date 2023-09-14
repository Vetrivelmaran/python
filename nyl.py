
#                                            interview quation
a =[
    ['luke','shaw'],
    ['wayne','rooney'],
    ['rooney','ronaldo'],
    ['shaw','rooney']
]
grnad_child =[]
per='ronaldo'
for i in a:
    if per in i:
        father =i[0]

for j in a:
    if father in j[1]:
        grnad_child.append(j[0])

print(len(grnad_child),'grandchildrens')
print(grnad_child)

