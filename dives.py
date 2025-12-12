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


def scores(difficulty):
    if difficulty >= 1.4 and difficulty <1.9: 
            probs=np.array([5,10,15,30,20,15,5])

            choice=np.random.choice(7,p=probs/100)

            match choice:
                case 0:
                    sco=np.arange(0,2.0,0.1)
                case 1: 
                    sco=np.arange(2.0,4.0,0.1)
                case 2:
                    sco=np.arange(4.0,5.5,0.1)
                case 3: 
                    sco=np.arange(5.5,6.5,0.1)
                case 4:
                    sco=np.arange(6.5,8.5,0.1)
                case 5: 
                    sco=np.arange(8.5,9.0,0.1)
                case 6: 
                    sco=np.arange(9.0,10.0,0.1)

            dive_score= np.random.choice(sco)
    
    elif difficulty >= 2.0 and difficulty <2.5:
            probs=np.array([5,8,15,25,25,17,5])

            choice=np.random.choice(7,p=probs/100)

            match choice:
                case 0:
                    sco=np.arange(0,2.0,0.1)
                case 1: 
                    sco=np.arange(2.0,4.0,0.1)
                case 2:
                    sco=np.arange(4.0,5.5,0.1)
                case 3: 
                    sco=np.arange(5.5,6.5,0.1)
                case 4:
                    sco=np.arange(6.5,8.5,0.1)
                case 5: 
                    sco=np.arange(8.5,9.0,0.1)
                case 6: 
                    sco=np.arange(9.0,10.0,0.1)

            dive_score= np.random.choice(sco)
    
    elif difficulty >= 2.5 and difficulty <3.0:
            probs=np.array([5,8,15,20,30,17,5])

            choice=np.random.choice(7,p=probs/100)

            match choice:
                case 0:
                    sco=np.arange(0,2.0,0.1)
                case 1: 
                    sco=np.arange(2.0,4.0,0.1)
                case 2:
                    sco=np.arange(4.0,5.5,0.1)
                case 3: 
                    sco=np.arange(5.5,6.5,0.1)
                case 4:
                    sco=np.arange(6.5,8.5,0.1)
                case 5: 
                    sco=np.arange(8.5,9.0,0.1)
                case 6: 
                    sco=np.arange(9.0,10.0,0.1)

            dive_score= np.random.choice(sco)
    
    elif difficulty >= 3.0 and difficulty <3.5:
            probs=np.array([5,8,17,20,30,15,5])

            choice=np.random.choice(7,p=probs/100)

            match choice:
                case 0:
                    sco=np.arange(0,2.0,0.1)
                case 1: 
                    sco=np.arange(2.0,4.0,0.1)
                case 2:
                    sco=np.arange(4.0,5.5,0.1)
                case 3: 
                    sco=np.arange(5.5,6.5,0.1)
                case 4:
                    sco=np.arange(6.5,8.5,0.1)
                case 5: 
                    sco=np.arange(8.5,9.0,0.1)
                case 6: 
                    sco=np.arange(9.0,10.0,0.1)

            dive_score= np.random.choice(sco)

    elif difficulty >= 3.5 and difficulty <4.0:
            probs=np.array([5,8,17,20,30,15,5])

            choice=np.random.choice(7,p=probs/100)

            match choice:
                case 0:
                    sco=np.arange(0,2.0,0.1)
                case 1: 
                    sco=np.arange(2.0,4.0,0.1)
                case 2:
                    sco=np.arange(4.0,5.5,0.1)
                case 3: 
                    sco=np.arange(5.5,6.5,0.1)
                case 4:
                    sco=np.arange(6.5,8.5,0.1)
                case 5: 
                    sco=np.arange(8.5,9.0,0.1)
                case 6: 
                    sco=np.arange(9.0,10.0,0.1)

            dive_score= np.random.choice(sco)

    elif difficulty >= 4.0 and difficulty <4.5:
            probs=np.array([5,8,17,20,30,15,5])

            choice=np.random.choice(7,p=probs/100)

            match choice:
                case 0:
                    sco=np.arange(0,2.0,0.1)
                case 1: 
                    sco=np.arange(2.0,4.0,0.1)
                case 2:
                    sco=np.arange(4.0,5.5,0.1)
                case 3: 
                    sco=np.arange(5.5,6.5,0.1)
                case 4:
                    sco=np.arange(6.5,8.5,0.1)
                case 5: 
                    sco=np.arange(8.5,9.0,0.1)
                case 6: 
                    sco=np.arange(9.0,10.0,0.1)

            dive_score= np.random.choice(sco)
    else: 
            probs=np.array([5,8,17,20,30,15,5])

            choice=np.random.choice(7,p=probs/100)

            match choice:
                case 0:
                    sco=np.arange(0,2.0,0.1)
                case 1: 
                    sco=np.arange(2.0,4.0,0.1)
                case 2:
                    sco=np.arange(4.0,5.5,0.1)
                case 3: 
                    sco=np.arange(5.5,6.5,0.1)
                case 4:
                    sco=np.arange(6.5,8.5,0.1)
                case 5: 
                    sco=np.arange(8.5,9.0,0.1)
                case 6: 
                    sco=np.arange(9.0,10.0,0.1)

            dive_score= np.random.choice(sco)

    return dive_score



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
