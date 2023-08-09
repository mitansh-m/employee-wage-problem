from random import randrange 

def presence() :
    x = randrange(0,3)
    return x 

def wage() :
    if presence() == 0 :
        x=0
    elif presence() == 1:
        x=20*8
    else : 
        x=20*4
    return x

print("daily employee wage is " + str(wage()))