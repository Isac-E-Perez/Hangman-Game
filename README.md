# Hangman Project
### About: 

For this project, I implemented an hangman game using Python. I used the libraries random and time which helped me to build the project. I used a combination of loops and functions to build this game.  

### Results:

First, I created the invite initiation for the start of the game.

```python
import random  # Generate pseudo-random numbers
import time  # Allows to handle various operations regarding time, its conversions and representations

# The starting screen
print("Hangman")  # Title: output string
name = input("Enter your name: ")  # made the variable 'name' equal the imput
print("Hello " + name + ". You got this! Start guessing the word!")  # Strings can be glued together with the +
time.sleep(2)  # function suspends (waits) execution of the current thread for a given number of seconds.
print("The game is about to start.")
time.sleep(3)
```

Afterwards, I defined the main function of the code. I defined the main function that initializes the arguments: global count, global display, global word, global already_guessed, global length and global play_game. They could be used further in other functions depending on how I want to call them.

```python
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
```

Then I developed the loop to execute the game multiple times.

```python
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
```

Including initialized conditions for hangman game. I call all the arguments again under the *hangman* function. The limit is used to set the maximum amount of guesses I provide to the user to guess a particular word.  

```python
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
```

Finally,  the rest of the hangman program combined together.

```python
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
```

If the letter is correclty guessed, index seraches for that letter in the word while display adds that letter in the given space according to its index or where itbelongs in the given word.

If the user guessed the wrong letter, the hangman starts to appear which also tells the user how many guesses are left. The count was initialized to zero and so with every wrong guess its  value increases with one where the limit is set to three. 

If the word is guessed correctly, matching the length of the display arguent, the user has won the game.

*main()* and *hangman()* would start again if the *play_loop* executes to yes and *play_loop* asks the user to play the game again or exit. 

### Final Product:

![Screen Shot 2021-10-04 at 1 30 01 PM](https://user-images.githubusercontent.com/89553126/135905110-0c1c1e9f-fef8-43d3-9ad0-186cb7a46ddc.png)

![Screen Shot 2021-10-04 at 1 30 19 PM](https://user-images.githubusercontent.com/89553126/135905112-529d1ca2-9bfe-47cd-8448-0595d0073117.png)

![Screen Shot 2021-10-04 at 1 30 40 PM](https://user-images.githubusercontent.com/89553126/135905116-ee1c690c-b48d-43ef-aba7-bbb261f33afe.png)

![Screen Shot 2021-10-04 at 1 31 26 PM](https://user-images.githubusercontent.com/89553126/135905117-4edea475-2307-4d85-866e-2e94af21c07b.png)

![Screen Shot 2021-10-04 at 1 31 34 PM](https://user-images.githubusercontent.com/89553126/135905119-3d97d080-ba6e-4bbc-aa05-bbab6d25bccc.png)
