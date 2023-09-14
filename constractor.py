class employee:
    def __init__(self,name,age,salry,role):
        self.name=name
        self.age=age
        self.salry=salry
        self.role=role   
    def detail_empl(self):
        print("the employee name is ",self.name)
        print("the employee age is ",self.age)
        print("the employee salry is ",self.salry)
        print("the employee role is ",self.role)
ob = employee('vetrive',21,400000,'python developer')        
print(list[ob.name,ob.age,ob.role,])
ob.detail_empl()
