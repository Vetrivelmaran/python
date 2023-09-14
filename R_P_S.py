import random
import time
def rps_game():
    print('*****this is rock papper scissor game****** ')
    print('1.rock \n2.pappor\n3.scissor')
    choose =int(input('choose the number 1-3  :'))
    if choose==1:
        print('you choose--> rock')
    elif choose==2:
        print('you choose-->pappor')
    elif choose==3:
        print('you choose-->scissor')
    else:
        print('wrong option')
        rps_game()
    print('michine choosing.......')
    time.sleep(3)
    machin = random.randint(1,3)
    print('machin choose-->',machin)

    if choose == machin:
        print('nice! , it is tie')
    elif choose ==1 and machin ==3:
        print('congradulation ! , you won ')
    elif choose==2 and machin==1:
         print('congradulation ! , you won ')
    elif choose==3 and machin==2:
         print('congradulation ! , you won ')
    else:
        print('machine won !,you loos the mach ')
    again =input('you want to play this game again (yes/no)').lower()

    if again=='yes':
        rps_game()

rps_game()