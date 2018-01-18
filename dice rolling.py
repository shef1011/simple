#Rolling Dice Game
import random
def dice_player():
    print('Rolling the dice Game! Lets Play')
    chance=random.randint(1,2)
    if chance==1:
        print("Welcome Player1! Roll dice")
        number1, number2 = (random.randint(1, 6), random.randint(1, 6))
        print(number1,number2)
    else:
        print("Welcome Player2! Roll dice")
        number1, number2 = (random.randint(1, 6), random.randint(1, 6))
        print(number1,number2)
    print('Next Player Roll dice')
    number3, number4 = (random.randint(1, 6), random.randint(1, 6))
    print(number3,number4)
    t,k=max(number1,number2,number3,number4)
    r,s=min(number1,number2,number3,number4)
    q,p=num_formed(t,r,k,s)
    if q==p:
        print("Match Over")
    elif q>p:
        print('Player1 won the match!Congrats')
    else:
        print('Player2 won the match!Congrats')
    print('Again Want to play?Yes or No?')
    t=input()
    if t=='Yes':
       dice_player()
    else:
        print('Game Finished')
def max(number1,number2,number3,number4):
    if number1>=number2:
        max=number1
    else:
        max=number2
    if number3>=number4:
        max1=number3
    else:
        max1=number4
    return max,max1
def min(number1,number2,number3,number4):
    if number1<=number2:
        min=number1
    else:
        min=number2
    if number3<=number4:
        min1=number3
    else:
        min1=number4
    return min,min1
def num_formed(t,k,r,s):
    x=t*10+k
    y=r*10+s
    return x,y

dice_player()