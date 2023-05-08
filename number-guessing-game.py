import random

while True:
    start = input('what is the starting range for the number? ')
    if start.isdigit():
        start = int(start)
        break
    else:
        print('enter only + numbers')
        continue

while True:
    stop = input("what is the stopping range for the number? ")
    if stop.isdigit():
        stop = int(stop)
        break
    else:
        print('enter only + numbers')
        continue


r = random.randrange(start,stop)



guesses = 1
while True:
        ans = input("guess for the number? ")
        if ans.isdigit():
            ans = int(ans)
        else:
                print("enter only + numbers")
                continue
            
            
        if ans == r:
                print('you guessed the correct number')
                print(f'it took you {guesses} guesses to answer')
                break


        else:
            print("you guessed the wrong number")
            guesses += 1
            if int(ans) > r:
                print('your guess was higher')
                continue
            else:
                print('your guess was lower')
                continue
       
            
                    
