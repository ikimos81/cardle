import random

def validateGuess(guess,colors,numbers):
    if len(guess)!=3:
        return False
    if guess[0] not in colors:
        return False
    if guess[1] not in colors.values() or colors[guess[0]]!=guess[1]:
        return False
    if guess[2] not in numbers:
        return False
    return True

def evaluateGuess(card1,guess1,card2,guess2,numbers):
    
    evaluation=[]
    eval1=[]
    eval2=[]

    corrCount=0

    for i in range(2):
        if card1[i]==guess1[i]:
            eval1.append('*')
            corrCount+=1
        elif guess1[i]==card2[i]:
            eval1.append('o')
        else:
            eval1.append('x')
            
        if card2[i]==guess2[i]:
            eval2.append('*')
            corrCount+=1
        elif guess2[i]==card1[i]:
            eval2.append('o')
        else:
            eval2.append('x')

    if numbers[card1[2]]>numbers[guess1[2]]:
        eval1.append('^')
    elif numbers[card1[2]]<numbers[guess1[2]]:
        eval1.append('v')
    else:
        eval1.append('*')
        corrCount+=1
        
    if numbers[card2[2]]>numbers[guess2[2]]:
        eval2.append('^')
    elif numbers[card2[2]]<numbers[guess2[2]]:
        eval2.append('v')
    else:
        eval2.append('*')
        corrCount+=1
        
    evaluation.append(eval1)
    evaluation.append(eval2)
    evaluation.append(corrCount)
    return evaluation

def parseFeedback(eg):
    print('\nCARD 1:\t\tCARD 2:')
    for elem in eg[0]:
        print(elem+' ',end='')
    print('\t\t',end='')
    for elem in eg[1]:
        print(elem+' ',end='')
    print('\n')
    
    if eg[2]==6:
        return '*'
    else:
        return ''
    

def cardleSession():
    colors={'H':'R','D':'R','S':'B','C':'B'}
    suits=['H','C','S','D']
    #TODO: handle the 10 elegantly
    numbers={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13}
    #[suit, color, number]
    #TODO: prevent two of the same card (low priority/probability)
    card1=[]
    card2=[]
    card1.append(suits[random.randint(0,len(suits)-1)])
    card1.append(colors[card1[0]])
    card1.append(random.choice(list(numbers.keys())))
    card2.append(suits[random.randint(0,len(suits)-1)])
    card2.append(colors[card2[0]])
    card2.append(random.choice(list(numbers.keys())))
    
    #print(card1)
    #print(card2)

    begin=''
    while begin!='B':
        begin=input('[set of rules I\'m too lazy to type]\nEnter B to begin, Q to quit:\n').upper()
        if begin=='Q':
            return
            
    win=''
    while win!='*':
        cardGuess1=''
        while not validateGuess(cardGuess1,colors,numbers):
            cardGuess1=input('Enter a valid guess for card 1 (suit,color,number): ').upper()
            if cardGuess1=='Q':
                return
            
        cardGuess2=''
        while not validateGuess(cardGuess2,colors,numbers):
            cardGuess2=input('Enter a valid guess for card 2 (suit,color,number): ').upper()
            if cardGuess2=='Q':
                return

        guess=evaluateGuess(card1,cardGuess1,card2,cardGuess2,numbers)
        win=parseFeedback(guess)

    print('YOU WIN!')


cardleSession()
