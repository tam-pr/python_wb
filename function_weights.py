import random
import numpy as np

def dive_difficulty(values):
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

def scores_14_19():
    values=[5,10,15,30,20,15,5]
    score=dive_difficulty(values)

    return score



def main():
    score=scores_14_19()
    print(score)

main()