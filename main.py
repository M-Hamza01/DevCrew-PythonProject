#python calculator
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# initializing and declaring the functions
def asfand_khan(): # main function that controls all the code named asfand_khan

   def add(a,b): # function for adding two numbers
    return a+b
   def subtract(a,b): # function for subtracting the two numbers
    return a-b
   def multiply(a,b): # function for multiplying two numbers
    return a*b
   def divide(a,b): # function for dividing two numbers
    return a/b

   while True:
    choice = input("Enter choice (1/2/3/4): \n") #stores input in choice

    if choice in ('1', '2', '3', '4'): #checks if the right numbers are entered if numbers are not right then else function runs and displays the output

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

    else:
        print("Invalid input. Please choose from 1, 2, 3, or 4.")

# loop runs forever it stops only when the user stops the program as the condition is always true so
# it makes possible for the user to perform multiple operations without restarting the code

asfand_khan() # calling the main function