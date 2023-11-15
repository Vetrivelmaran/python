def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
class Classname:
    a=45
    def __init__(self,a,b) -> None:
        self.name=a
        self.age=b
if __name__=="__main__":
    ob =Classname('vetri',82)
    print(ob.a)
    print(__name__)