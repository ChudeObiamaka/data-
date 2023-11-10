print("Welcome to the Guess the Number game")
print("Am thinking of a number beteween 1 and 100. Can you guess what is it?")
import random
random_number = random.randint(1, 100)
#Intialize Variables
guesses = 0
# Initialize a boolean variable
correct_guess = False
while not correct_guess: # Use the boolean variable as the loop condition
    player_guess = int(input("Enter your Guess "))
    #Increment the Number of Guesses
    guesses+=1
    if player_guess > random_number:
        print("Your guess is too high, Please try again ")
    elif player_guess < random_number:
        print("Your guess is too low, Please try again. ")
    else:
        print("Congratulations! You guessed the correct number ") 
        correct_guess = True # Set the boolean variable to True to exit the loop