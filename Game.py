import random

def gamewin(comp,you):
    if comp==you:
        return None
    elif comp =='R':
        if you=='S':
            return False
        elif you=='p':
            return True
    elif comp=='S':
        if you =='p':
            return False
        elif you=='R':
            return True
    elif comp=='P':
        if you =='R':
            return False
        elif you =='S':
            return True
            
                
                       
randno=random.randint(1,3)
if randno==1:
    comp='R'
elif randno==2:
    comp='S'
elif randno==3:
    comp='P'


you=input("your turn: Rock(R) Scissor(S) or Paper(P)? ")
a=gamewin(comp,you)

print(f"computer choose {comp}")
print(f"you choose{you}")

if a == None:
    print("the game is a tied")
elif a:
    print("you win")
else :
    print("you loose")