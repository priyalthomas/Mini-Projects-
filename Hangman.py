# Hangman game
import random
def choices():
    b=[]
    movies=['drive','lalaland','darkknight','churuli','prisoners','predator']
    rand=random.choice(movies)
    for i in rand:
        b.append(i)
    return b
def game(rand):
    userinput=[]  
    for i in rand:
        userinput.append(' ')
    chance=4
    while chance<0:
        u=input()
        for i in range(len(rand)):
           if rand[i]==u:
               userinput[i]=u  
        chance-=1
        print(userinput)        
        if len(u)>3:
            b=[]
            for i in u:
                b.append(i)
            if b==rand:
                print(b)
                print('success')
                break
            else:
                print('failed')
                break     
        print(f'you have {chance} left')
movies=choices()
game(movies)
