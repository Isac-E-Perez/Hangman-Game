import random  # Generate pseudo-random numbers
import time  # Allows to handle various operations regarding time, its conversions and representations

# The starting screen
print("Hangman")  # Title: output string
name = input("Enter your name: ")  # made the variable 'name' equal the imput
print("Hello " + name + ". You got this! Start guessing the word!")  # Strings can be glued together with the +
time.sleep(2)  # function suspends (waits) execution of the current thread for a given number of seconds.
print("The game is about to start.")
time.sleep(3)


def main():  # Global variable can be accessed inside or outside of the function.
    global count
    global screen
    global statement
    global again
    global lens
    global start
    hangman_words = ["python", "java", "computer", "languages", "career"]
    statement = random.choice(hangman_words)  # Returns a randomly selected value from the list
    lens = len(statement)  # length of the string
    count = 0  # starts at zero
    screen = '_' * lens  # strings can be repeated with *
    again = []  # provides the indices of the correctly guessed string
    start = ""

    # loop development


def start_loop():  # def marks the start of the function header. The function name to uniquely identify the function.
    global start
    start = input("Do you want to re-play? \n y = yes, \n n = no\n")
    while start not in ["y", "n", "Y", "N"]:  # list
        start = input("Do you want to play again? \nyes or no")
    if start == "y":
        main()
    elif start == "n":
        print("Gameover")
        exit()  # exit out of game

    # conditions for gameplay


def hangman():
    global count
    global screen
    global statement
    global again
    global start
    limit = 3  # amount of guesses
    the_guess = input("Hangman word: " + screen + "Enter your guess: \n")
    the_guess = the_guess.strip()  # method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
    if len(the_guess.strip()) == 0 or len(the_guess.strip()) >= 2 or the_guess <= "9":  # limiting the amount of strings inputted
        print("Try a better response. No integers.")
        hangman()

    elif the_guess in statement:
        again.extend([the_guess])  # method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
        index = statement.find(the_guess)  # method finds the first occurrence of the specified value.
        statement = statement[:index] + "_" + statement[index + 1:]  # an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
        screen = screen[:index] + the_guess + screen[index + 1:]
        print(screen + "\n")

    elif the_guess in again:
        print("Another letter")

    else:
        count += 1

    if count == 1:
        print("""\
                
                 --------
                 |      |
                 |      |
                 |
                 |
                 |
                 |
                _|_
                
                """)
        print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

    elif count == 2:
        time.sleep(1)
        print("""\
                 --------
                 |      |
                 |      |
                 |      o
                 |     /|\  
                 |
                 |
                _|_
                
                """)

    elif count == 3:
        time.sleep(2)
        print("""\
                 --------
                 |      |
                 |      |
                 |      o
                 |     /|\  
                 |      |
                 |     / -
                _|_
                
                """)

        print("Wrong guess. You lose!")
        print("The word was:  ", again, statement)  # printing out the functions again and statement
        start_loop()  # sends user back to the start of the start_loop
    if statement == '_' * lens:
        print("Lets go! You guessed correctly!")
        start_loop()

    elif count != limit:  # not equal to
        hangman()


main()  # calls back the main loop

hangman()
