# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Tharshini Subash
#              	 Anshita Nair
#               Sonika Madhu
# Section:      573
# Assignment:   Project
# Date:         25 November 2022
#
#ENGR

# As a team, we have gone through all required sections of the 
# tutorial, and each team member understands the material

#import packages 
def hangman():    
    import random
    
    drawings = ['''
         ----+
             |
             |
             |
             |
        =======''', '''
         ----+
         |   |
         O   |
             |
             |
             |
        =======''', '''
        ----+
        |   |
        O   |
        |   |
            |
            |
       =======''', '''
        ----+
        |   |
        O   |
       /|   |
            |
            |
       =======''', '''
        ----+
        |   |
        O   |
       /|\  |
            |
            |
       =======''', '''
        ----+
        |   |
        O   |
       /|\  |
       /    |
            |
       =======''', '''
        ----+
        |   |
        O   |
       /|\  |
       / \  |
            |
       ======='''
        ]
    
    #print(drawings[6])
    
    words = ['badger', 'kangaroo', 'mouse', 'evening', 'sunlight', 'picture', 'science', 'classroom', 'sweater', 'coding', 'aggies', 'whoop', 'teacher', 'wombat', 'llama', 'baboon', 'monkey', 
             'finger', 'holiday', 'winter', 'bracelet', 'femur', 'anatomy', 'biology', 'chemistry', 'necklace',
             'material', 'monster', 'humanity', 'defend', 'breakfast', 'expression', 'triangle', 'service',
             'visible', 'present', 'survivor', 'software', 'hardware', 'crusade', 'bowel', 'predator', 'poetry',
             'rational', 'objective', 'garbage', 'subway', 'fastfood', 'replace', 'philosophy', 'patent', 'wound',
             'knowledge', 'divide', 'subtract', 'public', 'convict', 'government', 'resolve', 'college', 'salmon']
    
    
    #create all functions
    def getword(words):
        '''
        This function uses the random package to randomly pick a word from the hardcoded list.
    
        '''    
        wordsindex = random.randint(0, len(words)-1)
        return words[wordsindex]
    
    def printman(wronglets, correctlets, secretword):
        '''
        This function prints the appropriate hangman drawing from the hardcoded list along with the dashes (blank and populated).
    
        '''
        print(drawings[len(wronglets)])
        print()
        
        #determines how many dashes are needed based on length of word
        dashes = '_' * len(secretword)
        
        #fill in the blanks with correct guesses 
        for i in range(len(secretword)):
            if secretword[i] in correctlets:
                dashes = dashes[:i] + secretword[i] + dashes[i+1:]
        #this loop prints dashes with spaces in between and replaces them with correct guesses
        for let in dashes:
            print(let, end = ' ')
        print()
    
    def CheckUserGuess(guessed):
        '''
        This functions checks if the user inputted a single letter in the alphabet or if they inputted a letter they have already guessed.
    
        '''
        while True:
            print()
            userguess = input("Guess a letter: ")
            
            while len(str(userguess)) >1 or str(userguess) not in 'abcdefghijklmnopqrstuvwxyz':
                userguess = input('Guess a single letter in the alphabet: ')
                if str(userguess) in guessed:
                    userguess = input("You have already guessed this letter. Try again: ")
              
            return userguess
    
            
    def roundtwo():
        '''
        This function is to check if the user wants to play again once the first round is over. Returns True or False boolean value.
    
        '''
        askuser = input("Do you want to play again (yes or no): ")
        if askuser == 'yes' or askuser =='Yes':
            return True 
        else:
            return False        
    
    
    print('LETS PLAY HANGMAN!')
    
    wronglets = ''
    correctlets = ''
    secretword = getword(words)
    #print(secretword)
    gameover = False
    
    while True:
        printman(wronglets, correctlets, secretword)
        
        
        #get guess from user using the CheckUserGuess function
    
        userguess = CheckUserGuess(wronglets + correctlets)
        if userguess in secretword:
            correctlets += userguess
            
            ### check if user guessed all the letters in the word###
            congrats = True
            for i in range(len(secretword)):
                if secretword[i] not in correctlets:
                    congrats = False
                    break
            if congrats:
                print('CONGRATS!!! YOU GUESSED IT! The word is', secretword)
                gameover=True
             
        
        else:
            wronglets += userguess
            
            ### check if the player has run out of guesses (the last hangman drawing already printed)
            if len(wronglets) == (len(drawings)-1):
                printman(wronglets, correctlets, secretword)
                print()
                print("womp womp :/ You have run out of guesses. The word is", secretword)
                gameover = True
                break
          
        ### Ask if the user wants to play again using the playagain function
        if gameover:
            if roundtwo():
                wronglets = ''
                correctlets = ''
                secretword = getword(words)
                gameover = False
                
            else:
                break


hangman()






