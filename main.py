import random

x = random.randint(0,9)

i = 0

correct = false

while i < 5:
    t = int(input("What's your guess?\n"))

    if t==x:
        correct = true
        break
    elif t < x:
        print('Incorrect Guess! ' + str(t) + ' Is lesser than the correct number!')
    
    elif t > x:
        print('Incorrect Guess! ' + str(t) + ' Is more than the correct number!')        
    
if correct == true:
    print('You Win!')
else:
    print('Maximum number of tries exceeded!')
