'''
Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
'''


def guessing_game():
    
    import random
    
    print("WELCOME TO GUESS ME!")
    print("I'm thinking of a number between 1 and 100")
    print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
    print("If your guess is within 10 of my number, I'll tell you you're WARM")
    print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
    print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
    print("LET'S PLAY!")
    
    num=random.randint(1,100)
    guess_list=[]                                                    #Creating lists for storing guesses and differences (to identify how far is the guess from no.)
    differences=[]
    while True:
    
        try:
            guess=int(input('Enter your guess (only an integer) :'))
        except:
            print('Please enter a valid integer')
            continue
        else:
            diff=abs(num-guess)
            guess_list.append(guess)
            differences.append(diff)
            if guess in range(1,101):
                if len(guess_list)==1 and len(differences)==1:           #Checking condition for first guess
                    if guess in range(num-10,num+11):
                        print('WARM')
                        continue
                    elif guess==num:
                        print('BINGO! You have won. It took you just 1 chance to guess correctly.')
                        break
                    else:
                        print('COLD')
                        continue
                elif len(guess_list)>1 and len(differences)>1:          #Checking condition for subsequent guesses
                    if guess==num and differences[-1]==0:
                        print('BINGO! You have won. It took you just %s chances to guess correctly.'%(len(guess_list)))
                        break
                    elif differences[-1]<=differences[-2]:
                        print('WARMER')
                        continue
                    else:
                        print('COLDER')
                        continue
                    
            else:
                print('OUT OF BOUNDS')
                continue
            break
            
guessing_game()