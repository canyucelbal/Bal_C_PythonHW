from random import randint
from gameFunctions import gameVars

def winorlose(status):
	print("******************")
	print("You",status, "!Would you like to play again")
	choice = input("Y / N? ")
	print(choice)

	if (choice is "Y") or (choice is "y"):
		#reset the game and start all over again
		gameVars.player_lives= 5
		gameVars.computer_lives= 5
		gameVars.total_lives= 5
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0,2)]

	elif (choice is "N") or (choice is "n"):
		print("You chose to quit quitter!")
		exit()
	else:
		print("Make a valid choice. Yes or no!")
		#recursion=> calling a function from inside itself
		winorlose(status)