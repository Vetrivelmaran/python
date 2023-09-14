

# multple inheritance

# the child class inherit more than one parent class 



class parent1:
    def data(self,stri1):
        self.stri1=stri1
    def show_st1(self):
        print(self.stri1)
class parent2:
    def data2(self,stri2):
        self.stri2 =stri2
    def show_st2(self):
        print(self.stri2)
class  child(parent1,parent2):        # ->>  here we inherit two parent class
    def data3(self,stri3):
        self.stri3=stri3
    def show_st3(self):
        print(self.stri3)
ob = child()                         # here we  creat object only for chiled class not for the parent claa
ob.data('one')
ob.data2('two')
ob.data3('tree')
ob.show_st1()
ob.show_st2()
ob.show_st3() 