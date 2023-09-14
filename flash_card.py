class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+f'({self.meaning})'
flash=[]
while(True):
    word =input('enter the name you want to add flashcard :')
    meaning =input('enter the meaning of flashcard :')
    flash.append(flashcard(word,meaning))
    choose =int(input('enter 0,if you want to continue\n'))
    if choose:
        break
for i in flash:
    print(i)
