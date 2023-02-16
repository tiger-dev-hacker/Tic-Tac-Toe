# Tic-Tac-Toe
Simulation of Tic-Tac-Toe game
Final Project Proposal – Tic Tac Toe
1.	Background– The project is based on the famous game Tic Tac Toe consisting of two players who use the symbols “0” and “X” respectively in 3X3 matrix. The player who can connect all his symbols either (“X” s or “0” s) in a pattern of three either vertically, horizontally, or diagonally in the 3X3 box is considered a winner.
2.	Simulation- The game environment will be simulated using Python in which the procedure of the game will occur as follows:
•	The two players will get a question prompt to start the game and the reply can be either yes or no.
•	Once the two players, the players will be selected randomly as to decide who gets to take the first turn.
•	The first player who takes a turn will decide which symbols to use (X or 0) and will get a prompt as to where to place his symbol. The board will be divided into a 3X3 matrix, with three rows and three columns i.e., nine spots in total. The user will decide the spot by specifying the row and the column in which he must place his symbol. 
•	After the first player gets a chance, the second player will place his other symbol (either 0 or X) in the remaining 8 spots (note: the second player will not be able to place his symbol where the first player has placed his symbol and will get an error.). The second player will also be able to decide the spot by specifying the row and the column where he wants the symbol to be placed.
•	This iterative process will continue till any player creates a pattern of three (i.e., either vertically, horizontally, or diagonally). Whosoever of the first player or second player creates the pattern first creates the pattern, he wins the game.
•	In case all the spots get filled up and neither of the player wins, program will display “Match drawn” and ask a prompt for the players to rematch or quit.
3.	Programming concepts:
•	Use of string structures, arrays, and lists to hold user input of symbols
•	Use of functions to simulate some properties such as player turns, place of symbols, etc. 
•	Use of loops and iterations (both finite and infinite) to prompt users to enter symbol in a spot, with 3 x 3 matrix shown each time that shows where the symbol is placed.
•	Use of conditional executions within loops to direct user the process of placing a symbol in a particular spot.
•	 Use of print and input statements with options to help players navigate through the game such as Play, Rematch, Help or Quit 

