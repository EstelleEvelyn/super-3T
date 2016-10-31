Super-Tic-Tac-Toe: Nine boxes, each containing its own tic-tac-toe board, contained within a "supergrid."

Super-Tic-Tac-Toe Rules:
Player one moves in the center box.
Player two moves in the box which corresponds to the square player one chose.
Play continues until one player has achieved three in a row in five boxes. 
Sending an opponent back to the center box when there are no legal moves in it automatically forfeits the game.

My Super-Tic-Tac-Toe program features a graphic interface which is designed to be fairly intuitive to use, with visual cues indicating when a box has been won and by whom, which box is legal to play in, etc. Gameplay can be between humans, or between a human and computer player.

It is structured so that information is passed from Box to Grid to Game to Interface.  In this manner, it is possible to store most necessary information as a list at the Box class level, and other classes need only reference and combine the information provide by classes lower in the hierarchy. 

The game runs without noticeable error in the 2-player version. While the 1-player version runs correctly, the AI is fairly simplistic because there are few widely accepted rules to this game, since only a handful of people know of it/how to play it

The program runs from the command line, opening a new graphics window and prompting the user to choose the one- or two-player option. Graphics.py must be in the same directory in order for the interface to function. After the one- or two- player prompt, the user need interact only with the graphics interface until the end of the game, at which point the winning player will be printed to the command line and prompt the user for input to exit. 