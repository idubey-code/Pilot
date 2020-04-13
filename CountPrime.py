'''
COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
'''

def count_primes(num):
    import math       
    count=0
    prime_list=[]
    def isprime(num1):                                      #Better way to check for primes
        if num1%2==0 and num1 > 2:
            return False
        for i in range(3,int(math.sqrt(num1)+1),2):
            if num1%i==0:
                return False
        return True
        
    for x in range(2,num):
        if isprime(x):
            count+=1
            prime_list.append(x)
    
    print(f'There are {count} prime numbers till {num}')
    print(f'They are:')
    print(prime_list)
    
while True:
    try:
        number=abs(int(input('Enter a number till which you need to count prime: ')))
    except:
        print('Please enter a valid number')
        continue
    else:
        count_primes(number)
        break
