import random

#This function prevents invalid user input, which could cause the program to crash.
def validationInput(message):
    number = 0
    while True:
        try:
            number = int(input(message))
            break # Exit the loop if the conversion is successful
        except ValueError:
            # Handle the error if the input cannot be converted to an integer
            print("Oops! That was no valid number. Try again...")
        except Exception as e:
            # Catch any other unexpected exceptions
            print(f"An unexpected error occurred: {e}")
    return number     
    
print("Welcome to Guessing Game! ")
lowBound = validationInput("Enter low bound: ")
highBound = validationInput("Enter high bound: ")

numApp = random.randint(lowBound, highBound)
guessCounter = 0

# This loop ensures the program keeps asking until the correct number is found.
while True:
    
    userNumber = validationInput("Enter your guess: ")
    guessCounter += 1

    if (userNumber < lowBound or userNumber > highBound):
        print(f"Invalid Number! Please, enter a number between {lowBound} and {highBound}")
    elif userNumber < numApp:
        print("Too low! Try a higher number.")
    elif userNumber > numApp:
        print("Too high! Try a lower number.")
    else:
        print(f"Correct! The number is {numApp}. You guessed it in {guessCounter} attempts.")
        break
