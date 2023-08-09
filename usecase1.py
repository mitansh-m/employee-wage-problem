from random import randrange 

def presence() :
    x = randrange(0,2)
    if x == 1 :
        print("present")
    else :
        print("absent")
    return x

def wage() :
    if presence() == 0 :
        x=0
    else :
        x=20*8
    return x

print("daily employee wage is " + str(wage()))