import random

computer_guess = random.randint(1,101)

print("computer guess " +  str(computer_guess ))

attempt= 0

def entry_point():

    level = input("please select a level - Type easy or hard  ")

    if(level == "easy"):

        attempt = 5

    else:

        attempt = 10

    attempt = str(attempt)

    print("You have " +attempt +  " attempts left")

    verify_guess(int(attempt))

def verify_guess(attempt):

    user_guess = int(input("guess  a number from one to hundred "))

    print("user guessed" + str(user_guess))

    if(computer_guess == user_guess):

        print("You have guessed the right number.")

        restart = input("Would you like to play again?. Say yes or no")

        if(restart == "yes"):

            entry_point()

        else:

            exit()

    elif(computer_guess > user_guess):

        print("You have gussed a lower number, try again")

        attempt -=  1

        attempt_check(attempt)

        verify_guess(attempt)

    else:

        print("You have gussed a higher number, try again")

        attempt -= 1

        print("you have " + str(attempt) + "attempts left")

        attempt_check(attempt)

        verify_guess(attempt)

def attempt_check(attempt):

    if(attempt == 0 ):

      start_over=   input("Sorry, no more attempts left . would you like to start over")

      if(start_over == "yes"):

          entry_point()

      else:

          exit()

         

entry_point()