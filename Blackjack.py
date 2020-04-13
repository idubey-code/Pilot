'''
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST
'''

print("Welcome to BLACKJACK !")

def blackjack(a,b,c):
    if a==11 or b==11 or c==11:
        if a+b+c<=21:
            print(a+b+c)
        else:
            if a+b+c-10<=21:
                print(a+b+c-10)
            else:
                print('BUST')
    else:
        if a+b+c<=21:
            print(a+b+c)
        else:
            print('BUST')

while True:
    try:
        num1=int(input('Enter first integer: '))
        num2=int(input('Enter first integer: '))
        num3=int(input('Enter first integer: '))
    except:
        print('Please enter a valid integer')
        continue
    else:
        blackjack(num1,num2,num3)
        break
