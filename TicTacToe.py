#Function to display board.
from IPython.display import clear_output
def display(input_list):
    clear_output()
    count=0
    print('\n')
    for i in range(0,9,3):
        count+=1
        if count!=3:
            print(f'{input_list[i]} | {input_list[i+1]} | {input_list[i+2]}\n---------')
        else:
            print(f'{input_list[i]} | {input_list[i+1]} | {input_list[i+2]}')
			
#Function to check winner.
def gamePlay(string,win,input_list2,position_list,marker,result_set):
    
    display(input_list2)
    
    while True:
        try:
            pos=int(input(f'\n{string}: Please enter the position to place marker : '))
        except:
            print('\nPlease enter valid position.')
            continue
        if pos not in range(1,10):
            print('Please enter valid position')
            continue
        elif pos in position_list:
            print('Position cannot be override. Please re-enter')
            continue
        else:
            break
                
    input_list2[pos-1]=marker

    for x in result_set:
        if input_list2[x[0]]==input_list2[x[1]]==input_list2[x[2]]==marker:
            win=True
            return win,marker,input_list2

    position_list.append(pos)
    
    return win,marker,input_list2
	
#Function to start game and give random chance.
import random
def game(p1,p2,input_list2):
    
    result_set=[(0,1,2),(0,3,6),(0,4,8),(1,4,7),(2,5,8),(3,4,5),(6,7,8),(6,4,2)]
    position_list=[]
    win=False
    chance=random.randint(0,1)
    
    while win==False and ' ' in input_list2:
        if chance==0:
            win,marker,input_list2=gamePlay('Player 1',win,input_list2,position_list,p1,result_set)
            chance+=1
        else:
            win,marker,input_list2=gamePlay('Player 2',win,input_list2,position_list,p2,result_set)
            chance-=1
    
    if win==False and ' ' not in input_list2:
        display(input_list2)
        return '\nIts a Tie !'
    
    if win==True and marker==p1:
        display(input_list2)
        return '\nPlayer 1 won !'
    elif win==True and marker==p2:
        display(input_list2)
        return '\nPlayer 2 won !'
    
#Front GUI function.
def ticTacToe():
    
    print('Welcome to Tic Tac Toe !')
    print('This game require 2 players.')
    print('Each player will get 3 chances.')
    print('Following is the board with position numbers:\n')
    
    print('1 | 2 | 3')
    print('---------')
    print('4 | 5 | 6')
    print('---------')
    print('7 | 8 | 9')
    
    print('\nTo place your marker, enter the position number when prompted')
    print("Let's Start !")

    while True:
        
        input_list2=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
        p1=str.lower(input('\nPlayer 1: Please select your marker (x or o) : '))
        p2=str.lower(input('Player 2: Please select your marker (x or o) : '))

        if p1 in ['x','o'] and p2 in ['x','o']:
            if p1==p2:
                print('\nTwo markers cannot be same. Please re-enter')
                continue        
        else:
            print('\nPlease enter valid markers')
            continue

        print(f'\nPlayer 1 : {p1}')
        print(f'Player 2 : {p2}')

        result=game(p1,p2,input_list2)
        print(result)
        del result
        choice=input("\nDo yo want to play again (Y/N) : ")
        
        if choice=='y' or choice=='Y':
            continue
        else:
            print('\nThank you !')
            break