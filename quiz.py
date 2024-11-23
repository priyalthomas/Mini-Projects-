import time
score=0
def options():
    a=time.time()
    user=input("")
    b=time.time()
    t=b-a
    if 5<=t:
       print("time up")
       return 0
    else:
       return user


def answer(a,b):
    score=0
    if a==b:
        print("Correct Answer")
        score+=50
    else:
        print("Incorrect Answer")
    return score
    
    
   
print("who is our father of our nation")
print("a.pablo\nb.heisenberg\nc.hitler\nd.gandhi ")
first=options()
score+=answer(first,'d')



print()
print(" what is 2+3")
print("a. 2\nb. -5\nc. 5\nd. 3")
second=options()
score+=answer(second,'c')



print("SCORE:   ",score)







