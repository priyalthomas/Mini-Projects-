import random
def roll():
    dice=random.randint(1,6)
    return dice
def  game():
    no=int(input("enter the number of players"))
    pos=[]
    for i in range(no):
        pos.append(0)
    while True:
        for i in range(no):
            input(f"player {i+1} enter to roll dice")
            rolldice=roll()
            print(rolldice)
            newpos=pos[i]+rolldice
            if newpos>100:
                print(newpos)
            else:
                if newpos==15:
                    newpos=7
                    print("snake",newpos)
                elif newpos==23:
                    newpos=3
                    print("snake",newpos)
                elif newpos==46:
                    newpos = 12
                    print("snake",newpos)
                elif newpos==62:
                    newpos=35
                    print("snake",newpos)
                elif newpos==90:
                    newpos=1
                    print("snake",newpos)
                elif newpos==3:
                    newpos=16
                    print("ladder",newpos)
                elif newpos==24:
                    newpos=82
                    print("ladder",newpos)
                elif newpos==32:
                    newpos=58
                    print("ladder",newpos)
                elif newpos==57:
                    newpos=73
                    print("ladder",newpos)
                elif newpos==68:
                    newpos=99
                    print("ladder",newpos)
                elif newpos==88:
                    newpos=91
                    print("ladder",newpos)
                pos[i]=newpos
                print(f'player {i+1} {newpos}')
                print()
                if newpos==100:
                    print('you won')
                    return
                    
game()     
         