#import the random package so we can generate a randon AI choice
from random import randint
from gameFunctions import winlose
from gameFunctions import gameVars
from gameFunctions import compare


while gameVars.player is False:
	print("*********************************\n")
	print("player lives: ", gameVars.player_lives, "/",gameVars.total_lives,"\n")
	print("computer lives: ", gameVars.computer_lives, "/",gameVars.total_lives,"\n")
	print("choose your weapon!\n")
	print("*********************************\n")

	gameVars.player = input("choose rock, paper or scissors\n")

	print("computer chose ", gameVars.computer, "\n")
	print("player choose ", gameVars.player, "\n")
	#start doing some logic and condition checking
	#print("\n computer: ", computer, "\n player: " , player )

	# -- this is where you would do the compare stuff
	compare.compareChoices(gameVars.computer,gameVars.player)
	
	#compare.compareChoices()
	
	#  -- end compare stuff

	#always check a breaking condition first
	# if player == gameVars.computer:
	# 	#we have a tie, no point in going any further
	# 	print("\n tie, no one wins! try again \n")

	# elif player == "quit":
	# 	print("\n you chose to quit quitter. \n")
	# 	exit()

	# elif player == "rock":
	# 	if gameVars.computer == "paper":
	# 		print("\n you lose!", gameVars.computer, "covers", player, "\n")
	# 		gameVars.player_lives = gameVars.player_lives -1
	# 	else:
	# 		print("\n you won!", player, "smashes", gameVars.computer, "\n")
	# 		gameVars.computer_lives = gameVars.computer_lives -1

	# elif player == "paper":
	# 	if gameVars.computer == "scissors":
	# 		print("\n you lose!", gameVars.computer, "cuts", player, "\n")
	# 		gameVars.player_lives = gameVars.player_lives -1
	# 	else:
	# 		print("\n you won!", player, "covers", gameVars.computer, "\n")
	# 		gameVars.computer_lives = gameVars.computer_lives -1

	# elif player == "scissors":
	# 	if gameVars.computer == "rock":
	# 		print("\n you lose!", gameVars.computer, "smashes", player, "\n")
	# 		gameVars.player_lives = gameVars.player_lives -1
	# 	else:
	# 		print("\n you won!", player, "cuts", gameVars.computer, "\n")
	# 		gameVars.computer_lives = gameVars.computer_lives -1

	if gameVars.player_lives is 0:
		winlose.winorlose("lost")
		#print("You lost! Loser. Would you like to play again?")
		# choice = input("Y / N?")

		# if choice == "Y" or choice == "y":
		# 	#reset the game and start all over again
		# 	player_lives = 1
		# 	computer_lives = 1
		# 	player = False
		# 	computer = choices[randint(0, 2)]
		# elif choice == "N" or choice == "n":
		# 	print("You chose to quit. Better luck next time!")
		# 	exit()
		# else:
		# 	print("Make a valid choice. Yes or no!")
			
	elif gameVars.computer_lives is 0:
		winlose.winorlose("win")
		#print("You won! Would you like to play again?")
		# choice = input("Y / N?")

		# if choice == "Y" or choice == "y":
		# 	#reset the game and start all over again
		# 	player_lives = 1
		# 	computer_lives = 1
		# 	player = False
		# 	computer = choices[randint(0, 2)]
		# elif choice == "N" or choice == "n":
		# 	print("You chose to quit. Better luck next time!")
		# 	exit()
		# else:
		# 	print("Make a valid choice. Yes or no!")
		# 	choice = input("Y / N?")
	else:
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0, 2)]	#else:
		#player = False
		#computer=choices[randint(0,2)]