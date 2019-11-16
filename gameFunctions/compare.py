from gameFunctions import gameVars

#need a function to run to compare the choices
#figure out what to pass into the function - hint => what are you comparing?
#
def compareChoices(gameVarscomputer,gameVarsplayer):
		#always check a breaking condition first
	if gameVars.computer == gameVars.player:
		#we have a tie, no point in going any further
		print ("tie! no one wins, play again")
	elif gameVars.player.lower() =="quit":
		exit()
	elif gameVars.player.lower() == "rock":
		if gameVars.computer == "paper":
			print("you lose!", gameVars.computer, "covers", gameVars.player,"\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("you win!", gameVars.player, "smashes through", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1
	elif gameVars.player.lower() == "paper":
		if gameVars.computer == "scissors":
			print("you lose!", gameVars.computer, "cuts", gameVars.player,"\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("you win!", gameVars.player, "coveres", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1
	elif gameVars.player.lower() == "scissors":
		if gameVars.computer == "rock":
			print("you lose!", gameVars.computer, "smashes", gameVars.player,"\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("you win!", gameVars.player, "cuts", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1
			
	else:
		print("that's not a valid choice, try again")