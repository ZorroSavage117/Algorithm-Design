# page start
import random
print()
# 1. Name:
#    Arlo Jolley
# 2. Assignment Name:
#    Lab 01: Guessing Game
# 3. Assignment Description:
#    Asks the user for a number and theny they have to guess a number and then display their guess and their amount of total guesses
# 4. What was the hardest part? Be as specific as possible.
#    Nothing was I have done a simular assinment before, so all I did was copy the old code in and changed some of it so it would complete the requirements for this assiment.
# 5. How long did it take for you to complete the assignment?
#    About 45 minutes.

# functions
# varables
my_num = 0
num_in = 0
guess = 0
guess_list = []
cont = ""
run_tf = True
game_tf = True
guess_num = 0
total_guesses = 0
num_games = 0
gpg = 0

# main code
print("This is the \"guesss a number\" game. \nYou try to guess a random number in the smallest number of attempts.\n")

while game_tf:

    guess = 0
    guess_num = 0
    guess_list = []

    num_in = int(input("Pick a positive integer: "))
    print(f"Guess a number between 1 and {num_in}")

    my_num = random.randint(1, num_in)

    while run_tf:
        guess = int(input("> "))
        guess_list.append(guess)

        if guess > my_num:
            print("        Too high!")
        elif guess < my_num:
            print("        Too low!")
        elif guess == my_num:
            # print("You got it.")
            run_tf = False

        guess_num = guess_num + 1

    print(f"You were able to find the number in {guess_num} guesses.")
    print(f"The numbers you guessed were: {guess_list}")

    cont = input("Do you want to play agian? ")

    if cont.lower() == "no" or cont.lower() == "n":
        game_tf = False
    else:
        run_tf = True

    num_games = num_games + 1
    total_guesses = total_guesses + guess_num
    del guess_list

gpg = total_guesses / num_games
print(f"You played {num_games} games.")
print(f"Your total number of guesses was {total_guesses}.")
print(f"Your guesses per game was {gpg}")

# page set up
print()
