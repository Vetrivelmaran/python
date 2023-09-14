
                                                       #multi level inheritance 
#           'it involve inheriting a class that has already some other clas'
class parent:                       #----> parent class
    def parent_data(self,name):               
        self.name=name
    def show_parent(self):
        return self.name
    

class chiled(parent):              #-----> chiled class . this class inherite atributes frome the parent class
    def child_data(self,age):
        self.age = age
    def show_chiled(self):
        return self.age
    


class grand_chiled(chiled):        #------> grand  child class . this class inherite atrubutes frome the child class
    def grand_data(self,waight):
        self.waight=waight
    def show_grand(self):
        return self.waight

ob = grand_chiled()                #------> we just creat object only for the grand child calass 
ob.parent_data('vetri')
ob.child_data(23)
ob.grand_data("120 cm")            #------> here the data assigement dor every class functions

print(ob.show_parent())          
print(ob.show_chiled())            #------> function caaling
print(ob.show_grand()
)

    
    

