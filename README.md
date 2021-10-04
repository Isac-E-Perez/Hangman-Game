# Hangman Project
### About: 

For this project, I implemented an hangman game using Python. I used the libraries random and time which helped me to build the project. I used a combination of loops and functions to build this game.  

### Results:

First, I created the invite initiation for the start of the game.

![Screen Shot 2021-10-04 at 1 00 05 PM](https://user-images.githubusercontent.com/89553126/135900955-8d9399ba-dd28-4cf1-be21-411eef82bf1e.png)

Afterwards, I defined the main function of the code. I defined the main function that initializes the arguments: global count, global display, global word, global already_guessed, global length and global play_game. They could be used further in other functions depending on how I want to call them.

![Screen Shot 2021-10-04 at 1 07 42 PM](https://user-images.githubusercontent.com/89553126/135901943-1dd268d9-70e3-4499-ad92-70cd0cfd2c4a.png)

Then I developed the loop to execute the game multiple times.

![Screen Shot 2021-10-04 at 1 08 59 PM](https://user-images.githubusercontent.com/89553126/135902105-8fec0b9f-5af7-4a80-894a-a83aa1317262.png)

Including initialized conditions for hangman game. I call all the arguments again under the *hangman* function. The limit is used to set the maximum amount of guesses I provide to the user to guess a particular word.  

![Screen Shot 2021-10-04 at 1 12 18 PM](https://user-images.githubusercontent.com/89553126/135902632-48c96627-77ad-42e7-a710-defcc1fed682.png)

Finally,  the rest of the hangman program combined together.

![Screen Shot 2021-10-04 at 1 12 30 PM](https://user-images.githubusercontent.com/89553126/135902635-eaaee6cc-6f5a-4153-b2bd-11a085e0f3fe.png)

![Screen Shot 2021-10-04 at 1 12 39 PM](https://user-images.githubusercontent.com/89553126/135902637-d46bd5d8-b227-4ccd-b9aa-008322dc4d62.png)

![Screen Shot 2021-10-04 at 1 12 53 PM](https://user-images.githubusercontent.com/89553126/135902638-1ed47b64-7445-45c4-87ba-cfade243b3e4.png)

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
