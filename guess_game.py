import random
"""This is a Number Guessing game where the computer generates a random Number between 1 and 50. The program also have the logic to play agin without exitng dependind upon the user"""
def playGame():
    secretNum = random.randint(1, 50)
    attempts = 0
    guess = None
    print("---------------------------------------------\n  Hey, welcome to the Number guessing Game!\n---------------------------------------------\n Let's check how good your Guessing is?\nWell you have to Guess a Number between 1 and 50\n\n If you guess the Number correctly, You WIN......\nLet's start!")
    while guess != secretNum:
        try:
            attempts+=1
            userInput = input("Enter the secret Number: " )
            guess = int(userInput)
            if guess > secretNum:
                print("Too High! Try lower")
            elif guess < secretNum:
                print("Too low! Try a higher number")
            
        except ValueError:
            print("Invalid Input! please enter a valid Number\n")
            continue
        
    print(f"\n\nCongrates! you have guessd the Secret Number\nYou are the savvy at gussing!\nYou guessed the Secret Number {secretNum} in {attempts} attempst.")
playGame()
def playAgain():
    play_again = "Yes"
    while 2 != 1:
        play_again = input("\n\nDo you want to play again(yes/no)")
        if play_again.lower().strip() == "yes":   
            playGame()
        elif play_again.lower().strip() == "no":
            print("Exitting....\nThanks for playing")
            break
playAgain()

