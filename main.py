#python calculator
import random

def printCalOption():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def add(a,b): # function for adding two numbers
    return a+b
def subtract(a,b): # function for subtracting the two numbers
    return a-b
def multiply(a,b): # function for multiplying two numbers
    return a*b
def divide(a,b): # function for dividing two numbers
    return a/b


# initializing and declaring the functions
def asfand_khan(): # main function that controls all the code named asfand_khan
   print("\n\n-----------------------\n|     Calculator     |\n-----------------------\n")
   while True:
        printCalOption()
        choice = input("\nEnter choice (1/2/3/4/5): ") #stores input in choice
        num1 = float(input("Enter first number: \n")) #allows the user to enter floating type numbers
        num2 = float(input("Enter second number: \n"))
        

        if choice == '1':
            print("result=",add(num1,num2)) #adds two numbers

        elif choice == '2':
            print("result=",subtract(num1,num2)) #subtracts two numbers

        elif choice == '3':
            print("print=",multiply(num1,num2)) #multiplies two numbers

        elif choice == '4':
            print("result=",divide(num1,num2)) #divides two numbers
        elif choice == '5':
            print("Exitting calculator....")
            break
        else: print("Invalid Input!")

# loop runs forever it stops only when the user stops the program as the condition is always true so
# it makes possible for the user to perform multiple operations without restarting the code



#------------------------
# Number Guessing game  |
#------------------------


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

def playAgain():
    playGame()
    play_again = "Yes"
    while 2 != 1:
        play_again = input("\n\nDo you want to play again(yes/no)")
        if play_again.lower().strip() == "yes":   
            playGame()
        elif play_again.lower().strip() == "no":    #strip() function is used to remove white spaces so that the input can be identified by the if statements
            print("Exitting....\nThanks for playing")
            break

def selectOption():
    while True:
        print("Hello! What do you want?" )
        print("1. calculator")
        print("2. Number Gussing Game")
        print("3. Exit")
        choice = input("Reply with 1, 2 or 3 : ")
        if choice =="1":
            asfand_khan()
        elif choice =="2":
            playAgain()
        elif choice =="3":
            break
        else: print("Invalid input!")

selectOption() #initatializing the process