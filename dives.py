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
        values=[5,8,17,20,30,15,5]
    
    else: 
        values=[5,8,17,20,30,15,5]

    score=weighter(values)
    return score

def next_score(score): 
    probs=np.array([15,15,15,12,12,8,7,5,5,3,3])
    choice=np.random.choice(11,p=probs/100)

    match choice:
        case 0:
            newscore=score
        case 1: 
            newscore=score+0.5
        case 2:
            newscore=score-0.5
        case 3: 
            newscore=score+1
        case 4:
            newscore=score-1
        case 5: 
            newscore=score+1.5
        case 6: 
            newscore=score-1.5
        case 7: 
            newscore=score+2
        case 8: 
            newscore=score-2
        case 9:
            newscore=score+2.5
        case 10: 
            newscore=score-2.5

    return newscore  

def sum_scores(score_array):
    min_score=min(score_array)
    max_score=max(score_array)
    sum_scores=sum(score_array)
    total=sum_scores - min_score - max_score
    
    return total

def final_score(total,difficulty):
    final_score= total*difficulty
    return final_score


def main(): 

    greeting()
    name,country=diver_1()
    dives=[]
    score_list=[]
    for i in range(5): 
        dive=dive_difficulty()
        dives.append(dive)
        print(dive)
    
        score=scores(dive)
        score_list.append(score)
        for i in range (6):
            score=next_score(score)
            score_list.append(score)
        
        total_sum=sum_scores(score_list)
        score_list.append(total_sum)
        total_score=final_score(total_sum,dive)
        score_list.append(total_score)
        print(total_sum)
        print(total_score)


main()