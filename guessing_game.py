# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sonika Reddy Madhu
# Section:      573
# Assignment:   10.14 LAB Guessing Game
# Date:         04 11 2022
#
#

#ENGR

def too_high(guess):
    #if guess > 26:
        print('Too high!')
        
    
def too_low(guess2):
    #if guess2 < 26:
        print('Too low!')
        

print("Guess the secret number! Hint: it's an integer between 1 and 100...")
input1 = input('What is your guess? ')

count = 0

#if input1 == 26:
    #print(f'You guessed it! It took you {counter} guesses.')
while True:
    #count += 1
    if input1 == 26:
        count+=1
        print(f'You guessed it! It took you {count} guesses.')
        break
    else:
        try:
            if int(input1) > 26:
                count += 1
                too_high(int(input1))
                input1 = int(input('What is your guess? '))
            else:
                count += 1
                too_low(int(input1))
                #count += 1
                input1 = int(input('What is your guess? '))
                #count += 1
        
        
        
        
        except ValueError:
            ##count =1
            #counter = count
            while input1 != 26 and input1 != '26':
                #counter += 1
                try:
                    if input1 == '26':
                        count += 1
                        print(f'You guessed it! It took you {count} guesses.')
                        break
                    
                    if input1.isnumeric():
                        #print(input1)
                        break
                    
                 
                    #count += 1
                    input1 = input('Bad input! Try again: ')
                    
                    
                   
                except:
                    input1 = input('Bad input! Try again: ')
                    #count += 1
            
            
            if input1 == '26':
                count += 1
                print(f'You guessed it! It took you {count} guesses.')
                break
            if int(input1) > 26:
                count+=1
                too_high(int(input1))
                input1 = int(input('What is your guess? '))
            elif int(input1) < 26:
                count+=1
                too_low(input1)
            elif int(input1)==26:
                count += 1
                print(f'You guessed it! It took you {count} guesses.')
                break
            #count += counter
            if input1 == '26':
                count+=1
                print(f'You guessed it! It took you {count} guesses.')
                break


    
    