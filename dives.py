import random
import numpy as np

def greeting(): 
    print("Bienvenidas y bienvenidos al torneo internacional de clavados de 2025")

def diver_1():
    name=input("Ingrese el nombre del clavadista: ")
    country=input("Ingrese el pais del clavadista: ")
    return name,country

def dive_difficulty():
    probs=np.array([5,10,15,30,20,15,5])

    choice=np.random.choice(7,p=probs/100)

    match choice:
        case 0:
            diff=np.arange(1.4,1.9,0.1)
        case 1: 
            diff=np.arange(2.0,2.5,0.1)
        case 2:
            diff=np.arange(2.5,3.0,0.1)
        case 3: 
            diff=np.arange(3.0,3.5,0.1)
        case 4:
            diff=np.arange(3.5,4.0,0.1)
        case 5: 
            diff=np.arange(4.0,4.5,0.1)
        case 6: 
            diff=np.arange(4.5,4.7,0.1)

    difficulty= np.random.choice(diff)
    return difficulty


def weighter(values):
    probs=np.array(values)

    choice=np.random.choice(7,p=probs/100)

    match choice:
        case 0:
            diff=np.arange(1.4,1.9,0.1)
        case 1: 
            diff=np.arange(2.0,2.5,0.1)
        case 2:
            diff=np.arange(2.5,3.0,0.1)
        case 3: 
            diff=np.arange(3.0,3.5,0.1)
        case 4:
            diff=np.arange(3.5,4.0,0.1)
        case 5: 
            diff=np.arange(4.0,4.5,0.1)
        case 6: 
            diff=np.arange(4.5,4.7,0.1)

    difficulty= np.random.choice(diff)
    return difficulty

def scores(difficulty):

    if difficulty >= 1.4 and difficulty <1.9: 
        values=[5,10,15,30,20,15,5]
    
    elif difficulty >= 2.0 and difficulty <2.5:
        values=[5,8,15,25,25,17,5]

    elif difficulty >= 2.5 and difficulty <3.0:
         values=[5,8,15,20,30,17,5]

    elif difficulty >= 3.0 and difficulty <3.5:
        values=[5,8,17,20,30,15,5]
    
    elif difficulty >= 3.5 and difficulty <4.0:
        values=[5,8,17,20,30,15,5]

    elif difficulty >= 4.0 and difficulty <4.5:
        values[5,8,17,20,30,15,5]
    
    else: 
        values=[5,8,17,20,30,15,5]

    score=weighter(values)
    return score


def main(): 

    greeting()
    name,country=diver_1()
    dives=[]
    score_list=[]
    for i in range(5): 
        dive=dive_difficulty()
        dives.append(dive)

        for i in range(7): 
            score=scores(dive)
            score_list.append(score)

main()
