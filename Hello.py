# I want to make a hangman game
# player 1 will enter in a word for the player to guess. 
# player 2 has head, both legs, and both arms (for a total of 5 lives).
# testing
# end goal is to have it pick from a list and randomly generate a hangman for me
# need to use a copy array so I can actually change the word
theWord = input("Enter in a word for the other player to guess! \n")
theWord = theWord.upper()
copytheWord = theWord
placeHolder = []
theWordLen = len(theWord)
winningScore = theWordLen

# This takes in an int
def reveal(index):
    placeHolder[index] = theWord[index]

# Use this to display the current updated board
def displayBoard(placeHolder):
        for n in placeHolder:
            print(n, end = " ")
        print("\n")

# Use this to create the first board
def createBoard(string):
    for n in range(theWordLen):
        placeHolder.append("_")
    displayBoard(placeHolder)
createBoard(theWord)

# Checks to see if string has any duplicated letters
def checkDupe(string):
    newWord = ""
    foundDupe = False
    # cant remove so I'ma just replace it lol
    #scroll through string, if the letter in string already exist in new word dont add
    for x in string:
        for y in newWord:
            if x == y:
                foundDupe = True
        if foundDupe == False:
            newWord = newWord + x
        elif foundDupe == True:
            foundDupe = False
    return newWord

# Displays all the incorrect guessed letters
def displayGuess(guessedLetters,lives):
    print("****************************")
    print("UPDATED LIST OF WRONG LETTERS: ")
    for n in guessedLetters:
        print(n, end = " ")
    print("\n")
    print("****Lives left: ",lives,"****")
    print("\n")



# Main
def main():
    lives = 5
    score = 0
    guessedLetters = []
    roundCounter = 0
    foundSomething = False
    win = False
    # I can do a for loop through theWord
    i = 0
    while i != 1:
        # make it so caps doesnt matter
        userInput = input("Please enter in your guess! \n")
        userInput = userInput.upper()
        userInput = checkDupe(userInput)
    

        # Check if the letter exist within the word
        for x in userInput:# H E L L O
            print(f"Round #{roundCounter}", end = " ") 
            theIndex = 0 # Using this instead of navigating through the string, it makes sense to me
            for y in theWord:
                if x == y:
                    reveal(theIndex)
                    foundSomething = True  
                    score = score + 1 
                theIndex = theIndex + 1

            if foundSomething == False:
                guessedLetters.append(x)
                lives = lives - 1
            roundCounter = roundCounter + 1
            displayBoard(placeHolder)
            displayGuess(guessedLetters,lives)
            foundSomething = False 
        if lives == 0:
            win = False
            break
        elif score == winningScore:
            win = True
            break       
    if win == True:
        print("Congratulations You Won!")
    elif win == False:
        print("Sorry, better luck next time!")
main()

