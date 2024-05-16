'''
Description:
        You must create a Guess the Word game that
        allows the user to play and guess a secret word.
        See the assignment description for details.
    
@author: christiankirby    cdk37
'''

import random
import os.path

def handleUserInputDifficulty():
    '''
    This function asks the user if they would like
    to play the game in (h)ard or (e)asy mode,
    then returns the corresponding number of misses
    allowed for the game.
    '''
    
    print("How many misses do you want? Hard has 8 and Easy has 12.")
    userinput = input("(h)ard or (e)asy> ")
    if userinput == "h":
        return int(8)
    elif userinput =="e":
        return int(12)





def getWord(words, length):
    '''
    Selects the secret word that the user must guess. 
    This is done by randomly selecting a word from words that is of length length.
    '''

    usuable_words = [word for word in words if len(word)== length]
    return random.choice(usuable_words)




def createDisplayString(lettersGuessed, missesLeft, guessedWordAsList):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''
    guessed_word_str = ' '.join(guessedWordAsList)
    guessed_letters_str = ' '.join(sorted(lettersGuessed))
    display_string = f"letters you've guessed: {guessed_letters_str}\nmisses remaining = {missesLeft}\n{guessed_word_str}"
    return display_string




def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''
    print(displayString)

    while True:
        userinput = input("letter> ")

        if len(userinput) == 1 and userinput.islower():
            if userinput not in lettersGuessed:
                return userinput
            else:
                print("you already guessed that")
        else:
            print("Invalid input. Please enter a letter")






def updateGuessedWordAsList(guessedLetter, secretWord, guessedWordAsList):
    '''
    Updates guessedWordAsList according to whether guessedLetter is in
    secretWord and where in secretWord guessedLetter is in.
    '''
    for i in range(len(secretWord)):
        if secretWord[i] == guessedLetter:
            guessedWordAsList[i] = guessedLetter
    return guessedWordAsList







def processUserGuess(guessedLetter, secretWord, guessedWordAsList, missesLeft):
    '''
    Uses the information in the parameters to update the user's progress in
    the Guess the Word game.
    '''
    print(updateGuessedWordAsList(guessedLetter, secretWord, guessedWordAsList))
    if guessedLetter in secretWord:
        updateGuessedWordAsList(guessedLetter, secretWord, guessedWordAsList)
        return [guessedWordAsList, missesLeft, True]
    else:
        missesLeft -= 1
        return [guessedWordAsList, missesLeft, False]




def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''
    f = open(filename)
    data = []
    for line in f:
        data.append(line.strip())
    f.close()
    misses_allowed = handleUserInputDifficulty()
    secret_word_length = random.randint(5, 10)
    secret_word = getWord(data, secret_word_length)  # Pass the result of
    # handleUserInputDifficulty to getWord
    guessed_word_as_list = ['_' for _ in range(secret_word_length)]
    letters_guessed = []
    misses_left = misses_allowed

    while True:
        # Display current game state
        display_string = createDisplayString(letters_guessed, misses_left,
                                             guessed_word_as_list)
        print(display_string)

        # Ask user to input a letter guess
        guessed_letter = handleUserInputLetterGuess(letters_guessed,
                                                    display_string)

        # Process user's guess
        result = processUserGuess(guessed_letter, secret_word,
                                  guessed_word_as_list, misses_left)
        guessed_word_as_list, misses_left, correct_guess = result

        # Add the guessed letter to the list of letters guessed
        letters_guessed.append(guessed_letter)

        # Check if the game is over
        if '_' not in guessed_word_as_list:
            print(f"Congratulations! You guessed the word: {secret_word}")
            print(
                f"You made {len(letters_guessed)} guesses with {misses_allowed - misses_left} misses.")
            return True
        elif misses_left <= 0:
            print(f"Game over! You're hung. The word was: {secret_word}")
            return False



if __name__ == "__main__":
    '''
    Running GuessWord.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
    '''
    runGame('lowerwords.txt')
    #print(getWord(data, 5))
