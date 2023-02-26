# RPS_GAME
 Rock Paper and Scissors Game

Welcome to Rock Paper Scissors. This Game produces result randomly using package random. 0: Rock, 1: Paper, 2: Scissors.

It defines functions to play the game, check if a user or machine wins, and display statistics about the game. 
The game() function is the main function that prompts the user for their choice and machine choice, calls check_win() to see if the user won, lost, or tied, and then prints the result. 
The display_stats() function prints out the number of wins, losses, ties, and win rate percentage of the user in the specified mode. 
The main() function calls the game() function and then displays the stats for the game. 
The logging module is also used to log warnings when the user enters invalid input.