# MinerSwep
 
MinerSwep is a game similar to minesweeper but with some changes made by me to make the game more dynamic and faster.

![responsive]()

## How To Play

 The game starts with a board with 8 columns and 8 rows. 4 bombs are planted randomly across the board and your duty is to guess where it will be safe to step . If you step on a bomb you lose.

 ![howtoplaymenu](https://github.com/dhardi/minerswep/blob/main/assets/images/howtoplay.PNG)

### Existing Features
  
- Menu of the Game:
  - Main menu
  - How To Play
  - Start

  ![Main Menu](https://github.com/dhardi/minerswep/blob/main/assets/images/menu_game.PNG)

## The Game 
 -the game consists of using arrays like the board and interacts depending on your input and placing eight numbers in each array eight will be our bomb if he selects that number he will lose the game if he makes eight attempts and manages to pass without selecting the bomb you will be the winner
   
 -Every turn, if your move does not locate the bomb on the display, a green icon will appear representing that you are safe.
  ![Gameplay](https://github.com/dhardi/minerswep/blob/main/assets/images/turn.PNG)


### Tips and Funfacts
  -A fun fact about Minesweeper, the classic computer game, is that it was created by Microsoft intern Robert Donner in 1989. The game was included in the Windows operating system starting from Windows 3.1, and it quickly became a popular pastime for many computer users. Despite its simple concept of clearing mines from a grid without detonating them, Minesweeper can be surprisingly addictive and challenging, leading to countless hours of gameplay for players around the world. Additionally, Minesweeper has inspired various competitions and even research into algorithmic strategies for solving the game efficiently.

 ![originalgame](https://github.com/dhardi/minerswep/blob/main/assets/images/minesweeper.png)

 ### End of cycle
   - The game ends if you step on one of the bombs or when you manage to go eight times without stepping on the bomb

  ![lost](https://github.com/dhardi/minerswep/blob/main/assets/images/lost.PNG)

  ### Win
   ![win](https://github.com/dhardi/minerswep/blob/main/assets/images/win.PNG)


  ### Error and bug handling
  - We have three stages of dealing with errors that may occur when the user enters data, first we check if the values are greater than in the column and row, the second stage we check if the input type is date and number or str and lastly we check if the values have already been entered by the user

## Diagram of the Game

-the diagram was initially created to create the data flow and how to deal with the information entered by the player was essential to have a better understanding of the scope of the game and its behaviors

![diagram](https://github.com/dhardi/minerswep/blob/main/assets/images/diagram.PNG)

## Future Ideas to Implement 

- level dificult 
- Timer
- system of guessing 
 

## Testing 
- During the development of this game I had several problems in creating the board, including dealing with input errors. Firstly, at the beginning of the project, I was trying to create a class and use it during the script, but it was not possible. I used a matrix system that consists of eight arrays that will interacting during the execution of the program, dealing with errors was also a challenge to execute my project because each interaction we have to treat the player's input at each stage.
-Throughout the project I created a second tab with the name test.py which was essential for the development of most of the tests and creation of methods out of this tab at the end of the project the final project all data from the test.py tab was copied to main tab run.py


### Validator Testing 



### Unfixed Bugs
- I had to use global Var one of my variables otherwise it will crash the game, i Know it not recommended to use Global variables.



## Deployment 
-The Site was Deployed to GitHub. The steps to deploy are as Fallows
-From the project's repository, go to the Settings tab.
-From the left-hand menu, select the Pages tab.
-Under the Source section, select the Main branch from the drop-down menu and click Save.
-A message will be displayed to indicate a successful deployment to GitHub pages and provide the live link.


## Credits

 -Firstly, I would like to mention my tutor who was a great help to my development, I would like to thank my wife for support. Below I will provide the links to the content to produce the website.

  - https://en.wikipedia.org/
  -https://www.delftstack.com/howto/python/python-clear-console/
  -https://www.fileformat.info/info/unicode/
  -https://pypi.org/project/pyfiglet/