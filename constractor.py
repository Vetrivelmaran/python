class robot():
    def __init__(self,n,a,w) -> None:
        self.name=n
        self.color=a
        self.weight=w
    def introduce(self):
        print(f'hello i am {self.name}')
    def idenity(self):
        print(f'you can idenify with my color {self.color}')
r1=robot('vetri','red',300)
# r1.name='vetri'
r2=robot('pravin','block',400)
r1.introduce()
r2.idenity()

