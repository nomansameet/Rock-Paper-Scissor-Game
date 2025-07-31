Project Title:
Rock, Paper, Scissors – A Terminal-Based Python Game

Project Description:
1. This is a simple, interactive Rock, Paper, Scissors game built using Python for the terminal.
2. The user competes against the computer by selecting Rock (0), Paper (1), or Scissors (2). 
3. The computer randomly selects one of the three choices, and the outcome is decided based on the classic game rules. 
4. To enhance the user experience, the project features ASCII art representations of each move.

1. User Input:

    The game begins by asking the user to input a number:
      0 for Rock
      1 for Paper
      2 for Scissors
    Input is converted to an integer and matched with corresponding ASCII art.

2. Computer Move:

    The computer randomly selects its move using random.randint(0, 2).

3. Visual Output:

    The user's and the computer's choices are printed as ASCII images from a predefined list.

4. Game Logic:

    The game uses if-elif statements to compare the user's choice and the computer's choice.

5. The rules are:

    Rock beats Scissors
    Scissors beats Paper
    Paper beats Rock
    If both choose the same: it's a Draw
    The logic checks for win, lose, or draw scenarios and displays the result.
