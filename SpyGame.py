'''
SPY GAME: FUNCTION THAT TAKES IN A LIST OF INTEGERS AND RETURNS TRUE IF IT CONTAINS 007 IN ORDER
'''

def spy_game(nums):
    nums2=[]                   #Empty list to extract 007 from the given list
    spy=[0,0,7]
    for x in nums:             #Iterating through given list and adding 007 to new one.
        if x==0 or x==7:
            nums2.append(x)
    if nums2==spy:             #Checking the lists for decision.
        print(True)
    else:
        print(False)
        
while True:
    try:
        string_input=input('Please enter atleast 3 numbers separated by space:\n ')
        string_list=string_input.split()
        number_list=list(map(int,string_list))
    except:
        print('You have not entered a valid pattern or an integer. Please refer the example:')
        print('10 20 30 40')
        print('Please try again in above format')
        continue
    else:
        spy_game(number_list)
        break
