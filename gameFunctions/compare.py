from gameFunctions import gameVars

#need a function to run to compare the choices
#figure out what to pass into the function - hint => what are you comparing?
#
def compareChoices()
		#always check a breaking condition first
	if player == gameVars.computer:
		#we have a tie, no point in going any further
		print("\n tie, no one wins! try again \n")

	elif player == "quit":
		print("\n you chose to quit quitter. \n")
		exit()

	elif player == "rock":
		if gameVars.computer == "paper":
			print("\n you lose!", gameVars.computer, "covers", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("\n you won!", player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "paper":
		if gameVars.computer == "scissors":
			print("\n you lose!", gameVars.computer, "cuts", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("\n you won!", player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "scissors":
		if gameVars.computer == "rock":
			print("\n you lose!", gameVars.computer, "smashes", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("\n you won!", player, "cuts", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1